import os
import traceback

import gradio as gr
import numpy as np
import timm
import torch
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms


# --------------------------------------------------
# Configuration
# --------------------------------------------------
MODEL_PATH = "best.pt"
MODEL_NAME = "convnextv2_tiny.fcmae_ft_in22k_in1k"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

CLASS_NAMES = [
    "Central Serous Chorioretinopathy",
    "Diabetic Retinopathy",
    "Disc Edema",
    "Glaucoma",
    "Healthy",
    "Macular Scar",
    "Myopia",
    "Pterygium",
    "Retinal Detachment",
    "Retinitis Pigmentosa",
]
NUM_CLASSES = len(CLASS_NAMES)


# --------------------------------------------------
# Preprocessing
# --------------------------------------------------
TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5] * 3, std=[0.5] * 3),
])


# --------------------------------------------------
# Model Loading
# --------------------------------------------------
def load_model() -> torch.nn.Module:
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}. "
            "Place best.pt in the same folder as app.py"
        )

    model = timm.create_model(
        MODEL_NAME,
        pretrained=False,
        num_classes=NUM_CLASSES,
    )

    state_dict = torch.load(MODEL_PATH, map_location=DEVICE)
    model.load_state_dict(state_dict)

    model.to(DEVICE)
    model.eval()
    return model


# --------------------------------------------------
# Grad-CAM
# --------------------------------------------------
FEATURE_MAP = None
GRADIENTS = None


def register_gradcam_hooks(model: torch.nn.Module) -> None:
    """
    Register hooks on the last stage of ConvNeXtV2 for Grad-CAM.
    """
    target_layer = model.stages[-1]

    def forward_hook(module, inputs, output):
        global FEATURE_MAP
        FEATURE_MAP = output

    def backward_hook(module, grad_input, grad_output):
        global GRADIENTS
        GRADIENTS = grad_output[0]

    target_layer.register_forward_hook(forward_hook)
    target_layer.register_full_backward_hook(backward_hook)


def generate_gradcam(
    model: torch.nn.Module,
    input_tensor: torch.Tensor,
    class_idx: int,
) -> np.ndarray:
    """
    Generate Grad-CAM heatmap for the target class.
    Returns a numpy array in [0, 1].
    """
    global FEATURE_MAP, GRADIENTS

    FEATURE_MAP = None
    GRADIENTS = None

    model.zero_grad()

    output = model(input_tensor)
    score = output[:, class_idx]
    score.backward()

    if FEATURE_MAP is None or GRADIENTS is None:
        raise RuntimeError("Grad-CAM hooks did not capture feature maps or gradients.")

    grads = GRADIENTS[0]   # [C, H, W]
    fmap = FEATURE_MAP[0]  # [C, H, W]

    weights = grads.mean(dim=(1, 2), keepdim=True)
    cam = (weights * fmap).sum(dim=0)
    cam = torch.relu(cam)

    cam = cam.detach().cpu().numpy()
    if cam.max() > 0:
        cam = cam / cam.max()

    return cam


def heatmap_to_rgb(cam: np.ndarray, size=(224, 224)) -> Image.Image:
    """
    Convert normalized CAM array to a pseudo-color PIL image.
    """
    cam_uint8 = np.uint8(cam * 255)

    red = cam_uint8
    green = np.uint8(np.clip(255 - np.abs(cam_uint8 - 128) * 2, 0, 255))
    blue = np.uint8(255 - cam_uint8)

    heatmap = np.stack([red, green, blue], axis=-1)
    return Image.fromarray(heatmap).resize(size)


def make_overlay(
    original_pil: Image.Image,
    heatmap_pil: Image.Image,
    alpha: float = 0.45,
) -> Image.Image:
    """
    Blend original image and heatmap.
    """
    original_resized = original_pil.convert("RGB").resize(heatmap_pil.size)
    return Image.blend(original_resized, heatmap_pil.convert("RGB"), alpha=alpha)


# --------------------------------------------------
# UI Formatting Helpers
# --------------------------------------------------
def format_top3_html(top3_idx, probs) -> str:
    rows = []
    medals = ["🥇", "🥈", "🥉"]

    for rank, idx in enumerate(top3_idx):
        rows.append(
            f"""
            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                gap:12px;
                padding:12px 14px;
                margin-bottom:10px;
                border:1px solid #e5e7eb;
                border-radius:14px;
                background:#ffffff;
                box-shadow:0 1px 2px rgba(0,0,0,0.04);
            ">
                <div style="
                    display:flex;
                    align-items:center;
                    gap:8px;
                    min-width:0;
                    flex:1;
                ">
                    <span style="font-size:18px; line-height:1;">
                        {medals[rank]}
                    </span>
                    <span style="
                        font-size:15px;
                        font-weight:700;
                        color:#111827;
                        line-height:1.4;
                        word-break:break-word;
                    ">
                        {CLASS_NAMES[idx]}
                    </span>
                </div>

                <div style="
                    flex-shrink:0;
                    padding:6px 10px;
                    border-radius:999px;
                    background:#f3f4f6;
                    border:1px solid #d1d5db;
                    font-family:monospace;
                    font-size:14px;
                    font-weight:800;
                    color:#111827;
                ">
                    {probs[idx]:.2f}
                </div>
            </div>
            """
        )

    return f"""
    <div style="
        background:#f8fafc;
        border:1px solid #e5e7eb;
        border-radius:18px;
        padding:16px;
        box-shadow:0 1px 3px rgba(0,0,0,0.06);
    ">
        <div style="
            font-size:18px;
            font-weight:800;
            margin-bottom:12px;
            color:#111827;
        ">
            Top-3 Predictions
        </div>

        <div style="
            font-size:13px;
            color:#6b7280;
            margin-bottom:12px;
            line-height:1.5;
        ">
            The three most likely classes predicted by the model.
        </div>

        {''.join(rows)}
    </div>
    """


def format_risk_html(risk: str) -> str:
    color_map = {
        "High": "#dc2626",
        "Medium": "#d97706",
        "Low": "#16a34a",
        "N/A": "#6b7280",
    }
    bg_map = {
        "High": "#fee2e2",
        "Medium": "#fef3c7",
        "Low": "#dcfce7",
        "N/A": "#f3f4f6",
    }

    color = color_map.get(risk, "#6b7280")
    bg = bg_map.get(risk, "#f3f4f6")

    return f"""
    <div style="
        background:#f9fafb;
        border:1px solid #e5e7eb;
        border-radius:16px;
        padding:14px;
        min-height:150px;
    ">
        <div style="
            font-size:18px;
            font-weight:700;
            margin-bottom:16px;
            color:#111827;
        ">
            Risk Level
        </div>
        <div style="
            display:inline-block;
            padding:10px 18px;
            border-radius:999px;
            background:{bg};
            color:{color};
            font-weight:800;
            font-size:18px;
            border:1px solid {color};
        ">
            {risk}
        </div>
    </div>
    """


def format_recommendation_html(risk: str, top1_class: str) -> str:
    if risk == "High":
        border_color = "#fca5a5"
        header_color = "#991b1b"
        badge_bg = "#fee2e2"
        badge_text = "#b91c1c"
        message = (
            "Ophthalmologist review recommended.<br>"
            "Further clinical examination is suggested."
        )
    elif risk == "Medium":
        border_color = "#fcd34d"
        header_color = "#92400e"
        badge_bg = "#fef3c7"
        badge_text = "#b45309"
        message = (
            "Moderate risk pattern detected.<br>"
            "Follow-up evaluation may be helpful."
        )
    else:
        border_color = "#86efac"
        header_color = "#166534"
        badge_bg = "#dcfce7"
        badge_text = "#15803d"
        message = (
            "Low-risk pattern detected.<br>"
            "Routine eye check is still recommended."
        )

    return f"""
    <div style="
        border:1px solid {border_color};
        border-radius:18px;
        background:#f8fafc;
        padding:16px;
        margin-top:10px;
        box-shadow:0 1px 3px rgba(0,0,0,0.06);
    ">
        <div style="
            display:flex;
            align-items:center;
            justify-content:space-between;
            margin-bottom:12px;
            gap:10px;
            flex-wrap:wrap;
        ">
            <div style="
                font-size:18px;
                font-weight:800;
                color:{header_color};
            ">
                Recommendation
            </div>

            <div style="
                padding:6px 12px;
                border-radius:999px;
                background:{badge_bg};
                color:{badge_text};
                font-size:13px;
                font-weight:700;
                border:1px solid {border_color};
            ">
                {risk} Risk
            </div>
        </div>

        <div style="
            background:#ffffff;
            border:1px solid #e5e7eb;
            border-radius:14px;
            padding:14px;
        ">
            <div style="
                font-size:14px;
                font-weight:700;
                color:#374151;
                margin-bottom:8px;
            ">
                Primary prediction
            </div>

            <div style="
                font-size:16px;
                font-weight:800;
                color:#111827;
                margin-bottom:14px;
            ">
                {top1_class}
            </div>

            <div style="
                font-size:15px;
                line-height:1.7;
                color:#1f2937;
            ">
                {message}
            </div>
        </div>
    </div>
    """


def format_empty_top3_html() -> str:
    return """
    <div style="
        padding:16px;
        border:1px solid #e5e7eb;
        border-radius:16px;
        background:#f9fafb;
        color:#111827;
    ">
        <b>Top-3 Predictions</b><br><br>
        No result yet
    </div>
    """


def format_info_html(message: str, border: str, background: str) -> str:
    return f"""
    <div style="
        padding:16px;
        border:1px solid {border};
        border-radius:16px;
        background:{background};
        color:#111827;
        line-height:1.6;
    ">
        {message}
    </div>
    """


# --------------------------------------------------
# App Startup
# --------------------------------------------------
MODEL = None
MODEL_STATUS = ""

try:
    MODEL = load_model()
    register_gradcam_hooks(MODEL)
    MODEL_STATUS = (
        f"✅ Model loaded successfully\n"
        f"- file: {MODEL_PATH}\n"
        f"- backbone: {MODEL_NAME}\n"
        f"- num_classes: {NUM_CLASSES}\n"
        f"- device: {DEVICE}"
    )
except Exception:
    MODEL = None
    MODEL_STATUS = (
        "❌ Model loading failed\n\n"
        f"{traceback.format_exc()}"
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------
def demo_predict(image):
    if image is None:
        return (
            format_empty_top3_html(),
            format_risk_html("N/A"),
            None,
            None,
            None,
            format_info_html(
                "Upload a fundus image and click <b>Predict</b>.",
                "#bfdbfe",
                "#eff6ff",
            ),
            MODEL_STATUS,
        )

    if MODEL is None:
        return (
            format_info_html(
                "<b>Prediction unavailable</b>",
                "#fecaca",
                "#fef2f2",
            ),
            format_risk_html("N/A"),
            image,
            None,
            None,
            format_info_html(
                "Model is not loaded.",
                "#fecaca",
                "#fef2f2",
            ),
            MODEL_STATUS,
        )

    original_image = image.convert("RGB")
    input_tensor = TRANSFORM(original_image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = MODEL(input_tensor)
        probs = F.softmax(outputs, dim=1)

    probs = probs.cpu().numpy()[0]

    top3_idx = probs.argsort()[-3:][::-1]
    top1_idx = int(top3_idx[0])
    top1_class = CLASS_NAMES[top1_idx]
    top1_prob = float(probs[top1_idx])

    if top1_prob >= 0.7:
        risk = "High"
    elif top1_prob >= 0.4:
        risk = "Medium"
    else:
        risk = "Low"

    heatmap_img = None
    overlay_img = None

    try:
        cam = generate_gradcam(MODEL, input_tensor, top1_idx)
        heatmap_img = heatmap_to_rgb(cam, size=original_image.size)
        overlay_img = make_overlay(original_image, heatmap_img, alpha=0.45)
    except Exception:
        heatmap_img = None
        overlay_img = None

    top3_html = format_top3_html(top3_idx, probs)
    risk_html = format_risk_html(risk)
    recommendation_html = format_recommendation_html(risk, top1_class)

    return (
        top3_html,
        risk_html,
        original_image,
        heatmap_img,
        overlay_img,
        recommendation_html,
        MODEL_STATUS,
    )


# --------------------------------------------------
# Gradio App
# --------------------------------------------------
with gr.Blocks(title="AI Fundus Analysis Prototype") as demo:
    gr.Markdown(
        """
        # AI Fundus Analysis Prototype
        Upload a retinal fundus image and review AI-based visual analysis results.

        **Output includes:** Top-3 prediction, risk level, Grad-CAM heatmap, overlay visualization, and recommendation.
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(type="pil", label="Upload Fundus Image")
            predict_btn = gr.Button("Predict", variant="primary")

        with gr.Column(scale=2):
            with gr.Row():
                top3_output = gr.HTML(label="Top-3 Predictions")
                risk_output = gr.HTML(label="Risk Level")

            with gr.Row():
                original_output = gr.Image(label="Original Image")
                heatmap_output = gr.Image(label="Grad-CAM Heatmap")
                overlay_output = gr.Image(label="Overlay Image")

    recommendation_output = gr.HTML(label="Recommendation")

    model_status_output = gr.Textbox(
        label="Model Load Status",
        value=MODEL_STATUS,
        lines=10,
        interactive=False,
    )

    gr.Markdown(
        """
        ---
        ### ⚠️ Disclaimer

        This is for research purposes only.  
        Not a medical diagnosis.  
        Consult a professional.
        """
    )

    predict_btn.click(
        fn=demo_predict,
        inputs=input_image,
        outputs=[
            top3_output,
            risk_output,
            original_output,
            heatmap_output,
            overlay_output,
            recommendation_output,
            model_status_output,
        ],
    )

demo.launch()