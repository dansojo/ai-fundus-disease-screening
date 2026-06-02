# Fundus Vision
### AI-Based Retinal Disease Screening and Explainable Analysis System

Fundus Vision is a portfolio project that demonstrates an AI-assisted retinal disease screening workflow using the Eye Disease Image Dataset. The project focuses on multi-class fundus image classification, class imbalance handling, model comparison, and Grad-CAM-based explainability.

This repository is intended primarily for project presentation and result sharing. It documents the workflow, experiments, visual analysis, and demo implementation created from Google Colab outputs.

### Quick Summary (KR)

- 안저 이미지를 10개 질환 클래스로 분류하는 AI 스크리닝 프로젝트입니다.
- 단순 정확도보다 클래스별 신뢰성, 불균형 대응, Grad-CAM 해석에 초점을 맞췄습니다.
- GitHub 저장소는 재현 패키지보다는 포트폴리오와 결과 공유 목적입니다.

---

## Project Overview

Retinal diseases such as diabetic retinopathy, glaucoma, and retinal detachment can lead to severe vision loss if they are not detected early. Large-scale screening is difficult in many clinical environments because expert review is limited and image characteristics vary across datasets.

This project builds an AI-assisted screening pipeline that classifies fundus images into 10 disease categories and provides visual explanations using Grad-CAM. The system is not intended to replace clinicians. It is designed as a research and educational prototype that shows how AI predictions can be paired with interpretable evidence.

### Quick Summary (KR)

- 조기 발견이 중요한 망막 질환을 AI로 선별하는 흐름을 구현했습니다.
- 10개 질환 분류 결과와 함께 Grad-CAM으로 판단 근거를 시각화했습니다.
- 의료진을 대체하는 모델이 아니라, 판단 보조와 설명 가능성 확인을 위한 연구형 시스템입니다.

### Key Features

- 10-class retinal disease classification
- Top-3 prediction output with probability scores
- Risk-level interpretation based on prediction confidence
- Class imbalance handling through two training strategies
- Class-wise performance analysis with confusion matrices
- Grad-CAM visual explanation for model reliability analysis
- Gradio-based interactive demo deployed on Hugging Face Spaces

### 핵심 기능 요약

- 안저 질환 10개 클래스 분류
- Top-3 예측과 확률 제공
- 예측 확률 기반 위험도 표시
- 클래스 불균형 대응 전략 비교
- 혼동 행렬과 클래스별 성능 분석
- Grad-CAM 기반 판단 근거 시각화
- Hugging Face Spaces 데모 제공

---

## Live Demo

[Fundus Vision Demo](https://huggingface.co/spaces/Danso0614/fundus-vision)

The live demo allows users to upload a fundus image and view:

- Top-3 disease predictions
- Confidence-based risk level
- Grad-CAM heatmap and overlay visualization
- Simple recommendation text for educational use

### Quick Summary (KR)

- 데모에서는 안저 이미지를 업로드해 예측 결과와 Grad-CAM 시각화를 확인할 수 있습니다.
- Top-3 질환 예측, 위험도, heatmap, overlay 결과를 함께 보여줍니다.
- 연구 및 학습 목적의 체험용 데모이며 실제 진단 도구가 아닙니다.

### Demo and Model Weight Policy

The demo code is included in [`demo/app.py`](demo/app.py), and it expects a model checkpoint named `best.pt`.

This GitHub repository does not include the trained model weight file. The `best.pt` checkpoint is managed only in the Hugging Face Space environment for the deployed demo. Therefore, cloning this repository alone is sufficient to review the project structure, notebooks, figures, metrics, and demo source code, but it is not intended to provide a fully runnable local inference package.

For dependency information related to the demo, see [`demo/requirements.txt`](demo/requirements.txt). A separate root-level `requirements.txt` is intentionally not provided because this repository is organized as a portfolio and result-sharing repository rather than a full reproducibility package.

### 모델 파일 관리 요약

- `demo/app.py`는 실행 시 `best.pt` 모델 가중치를 필요로 합니다.
- GitHub 저장소에는 `best.pt`를 포함하지 않습니다.
- 모델 가중치는 Hugging Face Space 환경에서만 관리됩니다.
- 이 저장소는 로컬 추론 실행보다 프로젝트 설명, 실험 결과, 산출물 공유에 초점을 둡니다.
- 데모 관련 의존성은 `demo/requirements.txt`에만 유지합니다.

---

## Problem Definition

Deep learning models can achieve strong classification performance on fundus image datasets, but high overall accuracy is not enough for medical AI analysis. In medical imaging, it is also important to understand whether the model focuses on clinically meaningful regions and whether performance is reliable across disease classes.

This project investigates three main questions:

- Can a lightweight model classify 10 fundus disease categories effectively?
- How does severe class imbalance affect model behavior?
- Do Grad-CAM results suggest that the model is focusing on clinically relevant regions?

### Quick Summary (KR)

- 의료 AI에서는 전체 정확도만으로 모델을 평가하기 어렵습니다.
- 클래스별 성능 차이, 불균형 영향, 오분류 패턴을 함께 봐야 합니다.
- Grad-CAM을 통해 모델이 실제 병변과 관련 있는 영역을 보는지 확인했습니다.

---

## System Architecture

The system follows a screening-style workflow:

1. Fundus image input
2. Image preprocessing
3. AI screening model inference
4. Top-3 disease prediction
5. Risk-level interpretation
6. Grad-CAM visual explanation
7. Human review support

### Quick Summary (KR)

- 입력 이미지를 전처리한 뒤 AI 모델이 질환 가능성을 예측합니다.
- 예측 결과는 Top-3 질환, 위험도, Grad-CAM 설명으로 구성됩니다.
- 최종 목적은 AI 결과를 사람이 이해하고 검토할 수 있게 만드는 것입니다.

<div align="center">
  <img src="https://github.com/user-attachments/assets/34a225aa-c58d-43b5-9e2a-fbebbeacc462" width="70%"/>
</div>

---

## Dataset

This project uses the Eye Disease Image Dataset, collected from multiple clinical sources.

### Data Source

- Anwara Hamida Eye Hospital
- BNS Zahrul Haque Eye Hospital
- Bangladesh

### Dataset Statistics

- Total images: 21,577
- Original images: 5,335
- Augmented images: 16,242
- Number of classes: 10

### Disease Classes

- Central Serous Chorioretinopathy
- Diabetic Retinopathy
- Disc Edema
- Glaucoma
- Healthy
- Macular Scar
- Myopia
- Pterygium
- Retinal Detachment
- Retinitis Pigmentosa

### Quick Summary (KR)

- 실제 병원 출처의 Eye Disease Image Dataset을 사용했습니다.
- 전체 21,577장 이미지로 구성되며, 원본과 증강 이미지가 함께 포함됩니다.
- 총 10개 안저 질환 클래스를 대상으로 분류 실험을 진행했습니다.

---

## Exploratory Data Analysis

EDA was conducted to understand dataset characteristics and identify issues that could affect model performance and generalization.

### Key Observations

- Severe class imbalance exists across disease categories.
- Image brightness and quality vary across samples.
- Augmented images are included and may influence distribution.
- Class-wise evaluation is important because the dataset is not uniformly balanced.

### Quick Summary (KR)

- 데이터셋은 클래스별 이미지 수 차이가 커서 불균형 문제가 존재합니다.
- 이미지 밝기, 품질, 해상도 차이가 있어 일반화 성능에 영향을 줄 수 있습니다.
- 따라서 전체 성능뿐 아니라 클래스별 성능 분석이 중요합니다.

### Class Distribution

<div align="center">
  <img src="figures/eda/class_distribution.png" width="70%"/><br/>
  <b>Class Distribution Across 10 Disease Categories</b>
</div>

### Sample Images

<div align="center">
  <img src="figures/eda/sample_images.png" width="85%"/><br/>
  <b>Representative Fundus Images for Each Class</b>
</div>

### Class Imbalance

<div align="center">
  <img src="figures/eda/class_imbalance.png" width="70%"/><br/>
  <b>Class Imbalance Distribution</b>
</div>

### RGB and Resolution Analysis

<div align="center">
  <img src="figures/eda/rgb_analysis.png" width="50%"/><br/>
  <b>RGB Channel Intensity Distribution</b>
</div>

<br/>

<div align="center">
  <img src="figures/eda/resolution_analysis.png" width="50%"/><br/>
  <b>Image Resolution Distribution</b>
</div>

---

## Model and Training Strategy

The model is based on ConvNeXtV2 Tiny. This architecture was selected because it provides a practical balance between performance and computational efficiency, especially for Google Colab-based experimentation.

### Training Setup

- Framework: PyTorch
- Backbone: ConvNeXtV2 Tiny
- Input size: 224 x 224
- Optimizer: AdamW
- Scheduler: CosineAnnealingLR
- Mixed Precision Training: enabled
- Transfer learning with pretrained ImageNet weights

### Quick Summary (KR)

- Google Colab 환경을 고려해 성능과 효율의 균형이 좋은 ConvNeXtV2 Tiny를 사용했습니다.
- PyTorch 기반 전이학습으로 학습을 진행했습니다.
- 입력 이미지는 224 x 224 크기로 맞추고, AdamW와 CosineAnnealingLR을 사용했습니다.

<div align="center">
  <img src="figures/architecture/ConvNext-Tiny-structure.png" width="75%"/><br/>
  <b>ConvNeXt-Tiny Architecture Overview</b>
</div>

### Class Imbalance Handling

Class imbalance was one of the most important challenges in this dataset. Two training strategies were compared:

#### Strategy A: Class Weight + Focal Loss

- Applies class weights to balance loss contribution
- Uses Focal Loss to focus learning on difficult samples
- Intended to reduce bias toward majority classes

#### Strategy B: Oversampling + Focal Loss

- Oversamples minority classes during training
- Uses Focal Loss for stable learning
- Intended to increase minority-class exposure

### 불균형 대응 요약

- Strategy A는 클래스 가중치와 Focal Loss로 다수 클래스 편향을 줄이는 방식입니다.
- Strategy B는 소수 클래스를 더 자주 학습시키는 oversampling 방식입니다.
- 두 전략을 비교해 불균형 상황에서 더 안정적인 학습 방법을 확인했습니다.

<div align="center">
  <img src="figures/results/experiment_design_diagram.png" width="70%"/><br/>
  <b>Training Strategy Comparison Pipeline</b>
</div>

---

## Experimental Results

The model achieved strong overall performance, but reliability varied by class. This makes class-wise analysis especially important for medical imaging tasks.

### Overall Performance

Best observed performance:

- Strategy A: Macro F1 approximately 0.90
- Strategy B: Macro F1 approximately 0.89

### Quick Summary (KR)

- 두 전략 모두 높은 성능을 보였지만, Strategy A가 더 안정적인 결과를 보였습니다.
- 최고 Macro F1은 약 0.90 수준입니다.
- 전체 성능이 높더라도 클래스별 신뢰도 차이는 남아 있었습니다.

<div align="center">
  <img src="figures/results/performance_summary_table.png" width="65%"/><br/>
  <b>Performance Summary of Training Strategies</b>
</div>

<br/>

<div align="center">
  <img src="figures/results/ab_overall_performance.png" width="65%"/><br/>
  <b>Overall Performance Comparison</b>
</div>

### Model Comparison Insight

Both strategies produced strong results. However, Strategy A, Class Weight + Focal Loss, showed more stable overall and class-wise behavior than the oversampling-based approach. Oversampling helped expose minority classes more often, but it may also increase repeated-sample effects and overfitting risk.

### 모델 비교 요약

- Class Weight + Focal Loss 방식이 전체 및 클래스별 성능에서 더 안정적이었습니다.
- Oversampling은 소수 클래스 노출을 늘리지만 반복 샘플로 인한 과적합 가능성이 있습니다.
- 의료 이미지에서는 평균 성능뿐 아니라 클래스별 안정성을 함께 보는 것이 중요합니다.

### Class-wise Performance

<div align="center">
  <img src="figures/results/classwise_f1_comparison.png" width="75%"/><br/>
  <b>Class-wise F1-score Comparison</b>
</div>

<br/>

<div align="center">
  <img src="figures/results/classwise_recall_comparison.png" width="75%"/><br/>
  <b>Class-wise Recall Comparison</b>
</div>

### Confusion Matrix Analysis

Row-normalized confusion matrices were used to compare class-wise prediction tendencies.

<table align="center">
  <tr>
    <td align="center">
      <img src="figures/results/confusion_matrix_norm_A_classweight_focal_g2.png" width="100%"/><br/>
      <b>A.</b> Class Weight + Focal Loss
    </td>
    <td align="center">
      <img src="figures/results/confusion_matrix_norm_B_oversample_focal_g2.png" width="100%"/><br/>
      <b>B.</b> Oversampling + Focal Loss
    </td>
  </tr>
</table>

### Confusion Matrix 요약

- 대부분의 클래스는 대각선 방향으로 강한 예측 안정성을 보였습니다.
- 시각적으로 유사한 질환 사이에서는 일부 오분류가 발생했습니다.
- 세밀하거나 모호한 특징을 가진 클래스는 더 신중한 해석이 필요합니다.

---

## Explainable AI with Grad-CAM

In medical imaging, explainability is important because model predictions need to be interpreted carefully. Grad-CAM was used to visualize which image regions influenced the model prediction.

The goal was not only to produce heatmaps, but also to assess whether attention patterns were clinically meaningful and consistent across disease categories.

### Quick Summary (KR)

- Grad-CAM으로 모델이 어떤 영역을 보고 예측했는지 확인했습니다.
- 높은 정확도만으로는 부족하므로, 판단 근거가 임상적으로 의미 있는지도 함께 봤습니다.
- 질환별로 attention의 안정성과 관련성이 다르게 나타났습니다.

### Example: Glaucoma

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/f1e9626a-b2bb-4a6f-aa82-54776ea61a8f" height="500"/><br/>
      <b>Original / Heatmap / Overlay Visualization</b>
    </td>
  </tr>
</table>

The model primarily focuses on the optic disc region when predicting glaucoma, which is clinically relevant because glaucoma is associated with structural changes around the optic disc. Some attention maps still spread beyond the target region, showing that the model has limitations in fine-grained localization.

### Glaucoma 해석 요약

- 녹내장은 시신경 유두 주변 구조 변화가 중요한 질환입니다.
- 모델은 대체로 optic disc 영역에 집중해 임상적으로 의미 있는 패턴을 보였습니다.
- 다만 일부 heatmap은 주변 영역으로 퍼져 세밀한 위치 해석에는 한계가 있습니다.

---

## Class-wise Model Reliability

Grad-CAM examples were grouped into reliability categories based on consistency, relevance, and focus.

### Good

- Diabetic Retinopathy
- Retinitis Pigmentosa
- Glaucoma

These classes showed relatively consistent focus on meaningful regions.

### Partial

- Macular Scar
- Central Serous Chorioretinopathy
- Disc Edema
- Retinal Detachment

These classes showed partially relevant but less stable attention patterns.

### Poor

- Pterygium
- Myopia
- Healthy

These classes showed weaker or less clinically meaningful focus in representative Grad-CAM examples.

### Quick Summary (KR)

- Good: 병변과 관련된 영역에 비교적 일관되게 집중했습니다.
- Partial: 일부 의미 있는 영역을 보지만 attention이 불안정했습니다.
- Poor: 질환 특징보다 불필요한 영역에 집중하거나 해석 신뢰도가 낮았습니다.
- 따라서 전체 성능만이 아니라 클래스별 설명 가능성까지 함께 확인해야 합니다.

<table align="center">
  <tr>
    <td align="center">
      <img src="figures/gradcam/Glaucoma_example.png" width="90%"/><br/>
      <b>Good</b><br/>
      Glaucoma
    </td>
    <td align="center">
      <img src="figures/gradcam/Disc Edema_example.png" width="90%"/><br/>
      <b>Partial</b><br/>
      Disc Edema
    </td>
    <td align="center">
      <img src="figures/gradcam/Myopia_example.png" width="90%"/><br/>
      <b>Poor</b><br/>
      Myopia
    </td>
  </tr>
</table>

---

## Limitations

- This project is for research, learning, and portfolio presentation only.
- The model is not a certified medical device.
- It should not be used as a replacement for medical diagnosis.
- Performance may vary under real-world image quality and dataset shifts.
- Some disease classes show unstable Grad-CAM attention.
- The repository does not include the trained model checkpoint.

### Quick Summary (KR)

- 본 프로젝트는 학습, 연구, 포트폴리오 목적입니다.
- 실제 의료 진단이나 임상 의사결정을 대체할 수 없습니다.
- 데이터셋 변화, 이미지 품질, 클래스별 특성에 따라 성능과 설명 결과가 달라질 수 있습니다.
- 모델 가중치 `best.pt`는 GitHub에 포함하지 않습니다.

---

## Future Work

- Improve reliability for underrepresented and visually ambiguous classes.
- Evaluate the model on external validation datasets.
- Compare Grad-CAM with additional explainability methods.
- Improve lesion-focused localization.
- Optimize inference for real-time deployment.
- Explore clinical decision-support integration in a validated setting.

### Quick Summary (KR)

- 소수 클래스와 시각적으로 모호한 질환의 성능을 개선해야 합니다.
- 외부 검증 데이터셋으로 일반화 성능을 확인할 필요가 있습니다.
- Grad-CAM 외의 설명 기법과 비교해 해석 신뢰도를 높일 수 있습니다.
- 실제 활용을 위해서는 속도, 안정성, 임상 검증이 추가로 필요합니다.

---

## Repository Structure

The repository is organized to preserve the current project workflow and Colab-generated outputs.

### Quick Summary (KR)

- `notebooks/`에는 Colab 기반 실험 과정이 정리되어 있습니다.
- `figures/`에는 README와 결과 설명에 사용되는 시각화 자료가 있습니다.
- `results/`에는 실험별 성능 지표 CSV가 있습니다.
- `demo/`에는 Hugging Face Space 데모 코드와 데모 의존성이 있습니다.

```text
ai-fundus-disease-screening
|
|-- README.md
|
|-- figures/
|   |-- architecture/
|   |   `-- ConvNext-Tiny-structure.png
|   |
|   |-- eda/
|   |   |-- class_distribution.png
|   |   |-- class_imbalance.png
|   |   |-- resolution_analysis.png
|   |   |-- rgb_analysis.png
|   |   `-- sample_images.png
|   |
|   |-- results/
|   |   |-- ab_overall_performance.png
|   |   |-- classwise_f1_comparison.png
|   |   |-- classwise_recall_comparison.png
|   |   |-- confusion_matrix_norm_A_classweight_focal_g2.png
|   |   |-- confusion_matrix_norm_B_oversample_focal_g2.png
|   |   |-- experiment_design_diagram.png
|   |   `-- performance_summary_table.png
|   |
|   `-- gradcam/
|       |-- Disc Edema_example.png
|       |-- Glaucoma_example.png
|       `-- Myopia_example.png
|
|-- notebooks/
|   |-- 01_EDA_and_Data_Preparation.ipynb
|   |-- 02_Baseline_Training_clean.ipynb
|   |-- 03_Experiment_A_ClassWeight_FocalLoss_clean.ipynb
|   `-- 04_Experiment_B_Oversampling_FocalLoss_clean.ipynb
|
|-- results/
|   |-- classification_report_A_classweight_focal_g2.csv
|   |-- classification_report_B_oversample_focal_g2.csv
|   |-- metrics_summary_A_classweight_focal_g2.csv
|   `-- metrics_summary_B_oversample_focal_g2.csv
|
`-- demo/
    |-- README.md
    |-- app.py
    `-- requirements.txt
```

---

## Notes

- The notebooks document the Google Colab-based workflow used to generate the project outputs.
- Figures and CSV files are retained as project artifacts for presentation and review.
- The Hugging Face Space manages the deployed demo environment and model checkpoint.
- This repository prioritizes clear project communication over full local reproducibility.

### Quick Summary (KR)

- 이 저장소는 결과와 역량을 보여주는 포트폴리오형 프로젝트 저장소입니다.
- 실험 산출물은 유지하고, 방문자가 흐름을 쉽게 이해하도록 구성했습니다.
- 모델 파일은 Hugging Face Space에서 관리하며 GitHub에는 포함하지 않습니다.
