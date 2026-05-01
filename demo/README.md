---
title: Fundus Vision
emoji: 🐨
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 6.10.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: AI-powered Retinal Disease Detection
---

# 🧠 AI Fundus Analysis Prototype

AI-powered retinal fundus image analysis demo with explainable predictions using Grad-CAM.

---

## 🔗 Live Demo

👉 Upload a fundus image and instantly see:

* Top-3 disease predictions
* Risk level assessment
* Visual explanation (Grad-CAM)

---

## 🚀 Features

### 1. Top-3 Predictions

Displays the three most probable classes with confidence scores.

```
1. Diabetic Retinopathy — 0.81  
2. Macular Scar — 0.12  
3. Healthy — 0.04  
```

---

### 2. Risk Level Assessment

Provides a simple risk interpretation based on model confidence:

* **High** → Immediate attention recommended
* **Medium** → Monitoring suggested
* **Low** → Likely normal

---

### 3. Visual Explainability (Grad-CAM)

The model highlights regions it focused on when making predictions.

* 🔴 Red = Highly influential region
* 🔵 Blue = Low influence

This helps interpret **why** the model made its decision.

---

### 4. Overlay Visualization

Combines the original image with the heatmap to make interpretation easier.

---

### 5. Recommendation System

Provides simple guidance based on prediction:

* Ophthalmologist review recommended
* Follow-up evaluation suggested
* Routine check advised

---

## 🖥️ How to Use

1. Upload a retinal fundus image
2. Click **Predict**
3. Review:

   * Predictions
   * Risk level
   * Heatmap & overlay
   * Recommendation

---

## 🧪 Model Details

* Backbone: ConvNeXtV2 (PyTorch / timm)
* Input size: 224 × 224
* Normalization: mean=0.5, std=0.5
* Output: 10-class classification

---

## 📊 Output Structure

| Component         | Description                     |
| ----------------- | ------------------------------- |
| Top-3 Predictions | Model confidence ranking        |
| Risk Level        | Confidence-based interpretation |
| Original Image    | Uploaded input                  |
| Heatmap           | Grad-CAM visualization          |
| Overlay           | Combined visualization          |
| Recommendation    | Action guidance                 |

---

## ⚠️ Disclaimer

This application is for **research and educational purposes only**.

* Not a medical diagnosis
* Not a clinical tool
* Always consult a qualified medical professional

---

## 🔍 Limitations

* Model may rely on non-lesion regions in some cases
* Performance depends on image quality
* Grad-CAM highlights **attention**, not exact pathology
* Not validated for real-world clinical use

---

## 🧠 Future Work

* Improve lesion-focused attention
* Class imbalance handling
* More robust explainability evaluation
* Clinical validation

---

## 💡 Key Insight

Prediction accuracy alone is not sufficient in medical AI.

This project emphasizes:
👉 **Explainability + Reliability**

---

## 📌 Notes

* Works best with clear fundus images
* Non-fundus images may produce unreliable results

---

## 🙌 Acknowledgement

This demo is built for showcasing:

* Computer vision skills
* Model deployment
* Explainable AI in medical imaging

---

