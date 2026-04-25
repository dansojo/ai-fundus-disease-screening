# 🩺 Fundus Vision  
### AI-Based Retinal Disease Screening & Explainable Analysis System

> AI-powered fundus disease classification with interpretability and clinical insight

---

# Project Overview

Retinal diseases such as diabetic retinopathy, glaucoma, and retinal detachment are major causes of vision loss worldwide. Early detection is essential for preventing irreversible damage, but large-scale screening remains challenging in many healthcare settings due to limited specialist availability.

This project presents an **AI-assisted fundus disease screening system** that classifies retinal fundus images into **10 disease categories** and provides **visual explanations using Grad-CAM**.

The system is designed not to replace medical diagnosis, but to support clinicians by identifying high-risk cases and providing interpretable prediction results.

---

## 🚀 Key Features

- **10-class retinal disease classification**
- **Top-3 prediction with probability scores**
- **Risk level assessment**
- **Grad-CAM-based visual explanation**
- **Class-wise performance analysis (Confusion Matrix)**
- **Gradio-based interactive demo**

---

## 💡 한눈에 보기 (Summary)

- 안저 이미지를 기반으로 **10가지 질환 분류**
- **Top-3 예측 + 위험도(Risk Level) 제공**
- **Grad-CAM을 통한 판단 근거 시각화**
- 의료진의 진단을 보조하는 **AI 스크리닝 시스템**

---

## 🎯 Project Focus

This project goes beyond simple classification and focuses on **model interpretability and reliability in medical imaging**.

---

# 🔗 Live Demo

👉 [🚀 Fundus Vision Demo 바로가기](https://huggingface.co/spaces/Danso0614/fundus-vision)

This demo allows users to experience the AI-based fundus disease screening system.

AI 기반 안저 질환 분류 및 설명 시스템을 직접 체험할 수 있습니다:

- 이미지를 업로드하여 질환 예측 결과 확인  
- Top-3 질환 예측 및 위험도 제공  
- Grad-CAM 기반 시각적 설명 확인  
---

# System Architecture

The overall system is designed to simulate a **real-world clinical screening workflow** using AI-assisted analysis.

본 시스템은 실제 의료 환경에서 활용 가능한 **AI 기반 안저 질환 스크리닝 흐름**을 반영하여 설계되었습니다.

---

<div align="center">
  <img src="https://github.com/user-attachments/assets/34a225aa-c58d-43b5-9e2a-fbebbeacc462" width="70%"/>
</div>

---

## 🔄 Workflow

The system follows a step-by-step pipeline:

본 시스템은 다음과 같은 단계로 동작합니다:

1. **Fundus Image Capture**  
   → 안저 카메라를 통해 환자의 망막 이미지 획득

2. **Hospital System / Upload**  
   → 병원 시스템 또는 플랫폼을 통해 이미지 업로드

3. **AI Screening Model**  
   → 딥러닝 모델이 입력 이미지를 분석

4. **Top-3 Disease Prediction**  
   → 가장 가능성이 높은 질환 3개를 확률과 함께 출력

5. **Explainable AI (Grad-CAM)**  
   → 모델이 판단한 근거를 시각적으로 제공

6. **Risk Score Assessment**  
   → 질환 위험도를 기반으로 추가 검사 필요성 판단

7. **Doctor Review**  
   → 의료진이 AI 결과를 참고하여 최종 판단 수행

---

## 💡 Key Insight

This architecture is not designed to replace doctors, but to **assist clinical decision-making by prioritizing high-risk cases and providing interpretable evidence**.

본 시스템은 의료진을 대체하는 것이 아니라,  
**고위험 환자를 선별하고 판단 근거를 제공하여 진단을 보조하는 역할**을 수행합니다.

---

# Problem Statement

While deep learning models have shown strong performance in fundus image classification, most approaches focus primarily on improving overall accuracy.

하지만 기존의 안저 이미지 분류 모델들은 높은 정확도를 달성하는 데 집중되어 있으며, 실제 의료 환경에서 중요한 문제는 충분히 다루지 못하고 있습니다.

---

### ❗ Key Challenges

- **Do models truly learn disease-specific features, or rely on spurious patterns?**  
  → 모델이 실제 병변을 이해하는가, 아니면 단순한 패턴에 의존하는가?

- **Can visually similar retinal diseases be reliably distinguished?**  
  → 시각적으로 유사한 질환을 안정적으로 구분할 수 있는가?

- **Are model predictions interpretable and trustworthy in a clinical context?**  
  → 모델의 예측 결과를 의료적으로 신뢰할 수 있는가?

---

### 🎯 Objective

This project aims to move beyond simple classification and focuses on evaluating **model reliability and interpretability**.

본 프로젝트는 단순한 분류 정확도를 넘어서,  
**모델의 판단 근거와 신뢰성을 분석하는 것**에 초점을 맞추고 있습니다.

To achieve this, we analyze model behavior using:

- Grad-CAM for visual explanation  
- Confusion matrix for class-wise reliability  
- Comparative experiments for imbalance handling  

---

The ultimate goal is to design an AI screening system that not only predicts diseases, but also provides **clinically meaningful and interpretable insights**.

---

# Dataset & Exploratory Data Analysis

## 📂 Dataset Overview

This project uses the **Eye Disease Image Dataset**, collected from multiple clinical sources.

> 본 프로젝트는 실제 병원에서 수집된 안저 이미지 데이터셋을 활용합니다.

---

### 🏥 Data Source

- Anwara Hamida Eye Hospital  
- BNS Zahrul Haque Eye Hospital  
- Bangladesh  

---

### 📊 Dataset Statistics

- **Total images:** 21,577  
- **Original images:** 5,335  
- **Augmented images:** 16,242  
- **Number of classes:** 10  

---

### 🧾 Disease Classes

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

---

### 📈 Data Distribution

<div align="center">
  <img src="figures/eda/class_distribution.png" width="70%"/><br/>
  <b>Class Distribution Across 10 Disease Categories</b>
</div>

---

### 🖼️ Sample Images

<div align="center">
  <img src="figures/eda/sample_images.png" width="85%"/><br/>
  <b>Representative Fundus Images for Each Class</b>
</div>

---

## 🔍 Exploratory Data Analysis

EDA was conducted to understand dataset characteristics and identify potential challenges that could impact model performance and generalization.

> 데이터의 특성과 모델 성능 및 일반화에 영향을 줄 수 있는 요소를 파악하기 위해 EDA를 수행했습니다.

---

### ⚠️ Key Observations

- **Severe class imbalance exists across disease categories**  
- **Image brightness and quality vary significantly**  
- **Augmented images are included and may affect distribution**

---

### 📊 Class Imbalance

<div align="center">
  <img src="figures/eda/class_imbalance.png" width="70%"/><br/>
  <b>Class Imbalance Distribution (Sorted)</b>
</div>

---

### 🎨 RGB Channel Analysis

<div align="center">
  <img src="figures/eda/rgb_analysis.png" width="50%"/><br/>
  <b>RGB Channel Intensity Distribution</b>
</div>

---

### 📐 Image Resolution Analysis

<div align="center">
  <img src="figures/eda/resolution_analysis.png" width="50%"/><br/>
  <b>Image Resolution Distribution</b>
</div>

---

### 💡 Summary

- 데이터셋은 클래스 간 불균형이 심하게 존재함  
- 이미지 품질(밝기, 대비)이 일정하지 않음  
- 증강 데이터가 포함되어 있어 분포 왜곡 가능성 존재  

→ 이러한 특성은 모델 학습뿐만 아니라 **일반화 성능에도 직접적인 영향을 미치는 주요 요인**임

---

# Model & Training Strategy

## 🧠 Model Architecture

The model is based on **ConvNeXtV2 Tiny**, which was selected not only for its strong performance but also for its computational efficiency.  
Considering the limited GPU resources (e.g., Google Colab environment), a lightweight architecture was chosen to ensure stable training and practical deployment feasibility.

본 프로젝트에서는 **ConvNeXtV2 Tiny** 모델을 사용하였으며,  
제한된 GPU 환경(예: Google Colab)을 고려하여 성능과 계산 효율을 동시에 만족할 수 있는 경량 구조를 선택하였습니다.

---

### ⚙️ Training Setup

- **Framework:** PyTorch  
- **Input size:** 224 × 224  
- **Optimizer:** AdamW  
- **Scheduler:** CosineAnnealingLR  
- **Mixed Precision Training (AMP):** Enabled  

The model was trained using **transfer learning with pretrained ImageNet weights**, allowing faster convergence and improved generalization.

---

<div align="center">
  <img src="figures/architecture/A-ConvNext-Tiny-network-structure_B-ConvNext-Block-structure.png" width="75%"/><br/>
  <b>ConvNeXt-Tiny Architecture Overview</b>
</div>

---

## ⚠️ Challenge: Class Imbalance

During data analysis, **severe class imbalance** was identified as a major challenge affecting model performance.

데이터 분석 과정에서 클래스 간 데이터 수 불균형이 심하게 존재하는 것을 확인하였으며, 이는 모델의 편향을 유발할 수 있는 주요 문제로 판단되었습니다.

---

## 🧪 Training Strategies

To address this issue, two different approaches were explored:

---

### 🔹 Strategy A: Class Weight + Focal Loss

**Goal:**  
Reduce bias toward majority classes and focus learning on difficult samples.

- Class weights were applied to balance loss contribution  
- Focal Loss was used to emphasize hard examples  

---

### 🔹 Strategy B: Oversampling + Focal Loss

**Goal:**  
Increase minority class representation during training.

- Minority classes were oversampled  
- Focal Loss applied for stable learning  

---

<div align="center">
  <img src="figures/results/experiment_design_diagram.png" width="70%"/><br/>
  <b>Training Strategy Comparison Pipeline</b>
</div>

---

### 💡 Summary

- Class imbalance was the primary challenge in this dataset  
- Two complementary strategies were tested to address it  
- These approaches are further compared in the Results section

---

# Results & Model Analysis

## 📊 Overall Performance

The model achieved strong performance across all classes, showing its ability to classify retinal diseases effectively.

본 모델은 전반적으로 높은 성능을 보였으며, 다양한 안저 질환을 효과적으로 분류할 수 있음을 확인하였습니다.

- **Accuracy**
- **Precision**
- **Recall**
- **Macro F1 Score**

👉 Best performance: **Macro F1 ≈ 0.90**

---

## ⚖️ Training Strategy Comparison

To address class imbalance, two strategies were evaluated:

- **Strategy A:** Class Weight + Focal Loss  
- **Strategy B:** Oversampling + Focal Loss  

<div align="center">
  <img src="figures/results/performance_summary_table.png" width="65%"/><br/>
  <b>Performance Summary of Training Strategies</b>
</div>

<br/>

<div align="center">
  <img src="figures/results/ab_overall_performance.png" width="65%"/><br/>
  <b>Overall Performance Comparison (A vs B)</b>
</div>

---

### 💡 Strategy Insight

Both strategies achieved strong overall performance.  
However, **Class Weight + Focal Loss (Strategy A)** showed more stable and consistent results compared to the oversampling-based approach.

두 전략 모두 높은 성능을 보였지만,  
**Class Weight + Focal Loss 방식이 더 안정적인 성능**을 보였습니다.

Oversampling helped increase minority class exposure, but it also introduced potential noise and overfitting due to repeated samples.

---

## 📈 Class-wise Performance

In addition to overall metrics, class-wise performance was analyzed to understand how each strategy affected individual disease categories.

전체 성능뿐만 아니라, 각 질환 클래스별 성능 차이를 확인하기 위해 클래스별 F1-score와 Recall을 비교하였습니다.

<div align="center">
  <img src="figures/results/classwise_f1_comparison.png" width="75%"/><br/>
  <b>Class-wise F1-score Comparison</b>
</div>

<br/>

<div align="center">
  <img src="figures/results/classwise_recall_comparison.png" width="75%"/><br/>
  <b>Class-wise Recall Comparison</b>
</div>

---

### 🔎 Class-wise Observation

- Some classes achieved consistently high scores across both strategies  
- Certain minority or visually ambiguous classes showed larger performance variation  
- Strategy A generally provided more stable class-wise performance  

→ 클래스별 성능을 비교한 결과, 일부 질환은 안정적으로 분류되었지만  
시각적으로 유사하거나 데이터 수가 적은 클래스에서는 성능 편차가 존재했습니다.

---

## 🔍 Confusion Matrix Analysis

The confusion matrix was used to analyze class-wise prediction behavior and misclassification patterns.  
Row-normalized matrices were used to better compare prediction tendencies across classes.

혼동 행렬을 통해 클래스별 예측 패턴과 오분류 경향을 분석하였습니다.

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/2ec06c01-e053-4371-a0b0-8c6a50f3bc1b" width="100%"/><br/>
      <b>A.</b> Class Weight + Focal Loss
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/da8a03c8-7009-48e9-8edc-63fc0e21beab" width="100%"/><br/>
      <b>B.</b> Oversampling + Focal Loss
    </td>
  </tr>
</table>

---

### ⚠️ Confusion Patterns

- Most classes show strong classification performance with high diagonal dominance  
- Misclassification mainly occurs among visually similar disease classes  
- Some confusion appears between classes with similar lesion locations or overlapping anatomical regions  

→ 전체적으로는 높은 분류 성능을 보였지만,  
시각적으로 유사한 질환 간에서는 일부 혼동이 발생했습니다.

---

## 💡 Final Insight

Although the model achieved strong overall performance, reliability was not uniform across all classes.

The results suggest that overall accuracy alone is not sufficient for evaluating medical AI models.  
Class-wise analysis, confusion matrix interpretation, and Grad-CAM visualization are necessary to understand model reliability more deeply.

단순한 전체 정확도만으로는 의료 AI 모델의 신뢰성을 충분히 평가하기 어렵습니다.  
따라서 클래스별 성능 분석, 혼동 행렬, Grad-CAM 해석을 함께 활용하는 것이 중요합니다.

---

## 🔗 Next Step

These findings are further analyzed using **Grad-CAM** in the next section to understand **where the model is focusing** during prediction.

---

# Explainable AI

In medical imaging, high accuracy alone is not sufficient — understanding **why the model makes a prediction** is equally important.

의료 영상 분야에서는 단순한 정확도뿐만 아니라,  
**모델이 어떤 근거로 판단을 내렸는지**를 이해하는 것이 매우 중요합니다.

To address this, **Grad-CAM** was applied to visualize the image regions that influenced model predictions.

This allows us to verify whether the model focuses on clinically relevant regions rather than relying on irrelevant patterns.

Grad-CAM을 통해 모델이 실제로 어떤 영역을 보고 판단하는지 시각적으로 확인할 수 있습니다.

---

## Example: Glaucoma

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/f1e9626a-b2bb-4a6f-aa82-54776ea61a8f" height="500"/><br/>
      <b>Original / Heatmap / Overlay Visualization (5 Samples)</b>
    </td>
  </tr>
</table>

<p align="center">
The model primarily focuses on the optic disc region when predicting glaucoma.
</p>

---

### Interpretation

Glaucoma is characterized by structural changes in the optic disc, particularly an increased cup-to-disc ratio.

The Grad-CAM visualization indicates that the model consistently focuses on the optic disc region, suggesting that it has learned clinically relevant features.  
However, in some cases, the attention is diffused beyond the target region, indicating limitations in capturing fine-grained structural details.

---

### 💡 한눈에 보기

- 녹내장은 시신경 유두(Optic Disc)의 구조적 변화가 중요한 질환  
- 모델은 주요 병변 위치를 정확히 포착하고 있음  
- 일부 경우에서는 불필요한 영역까지 확장되는 경향 존재  

→ 전반적으로는 올바른 특징을 학습했지만, 세밀한 구조 인식에는 한계가 있음

---

These observations suggest that while the model captures meaningful regions,  
its reliability may vary across different disease categories.

→ 이러한 결과는 클래스별로 모델의 신뢰도가 다를 수 있음을 시사합니다.
---

# Class-wise Model Reliability Analysis

Based on Grad-CAM visualizations, we evaluated how reliably the model identifies disease-specific features for each class.

Grad-CAM 결과를 기반으로, 모델이 각 질환의 특징을 얼마나 안정적으로 인식하는지 평가하였습니다.

---

## 🧪 Evaluation Criteria

- **Consistency**: 동일 클래스에서 일관된 영역을 보는가  
- **Relevance**: 실제 병변 위치를 보는가  
- **Focus**: 불필요한 영역으로 확산되지 않는가  

---

## 📊 Reliability Categories

### 🟢 Good (Reliable)

- Diabetic Retinopathy  
- Retinitis Pigmentosa  
- Glaucoma  

→ 모델이 병변 위치를 정확하고 일관되게 집중함

---

### 🟡 Partial (Unstable)

- Macular Scar  
- Central Serous Chorioretinopathy  
- Disc Edema  
- Retinal Detachment  

→ 병변을 일부 인식하지만, 집중 영역이 불안정함

---

### 🔴 Poor (Unreliable)

- Pterygium  
- Myopia  
- Healthy  

→ 의미 있는 특징을 제대로 포착하지 못하거나 불필요한 영역에 집중함

---

## 💡 Key Insight

The analysis reveals that model performance is not uniform across classes.

Diseases with strong and distinctive visual patterns are learned effectively,  
while those with subtle or ambiguous features show unstable attention behavior.

→ 시각적 특징이 뚜렷한 질환은 잘 학습되었지만,  
애매한 특징을 가진 질환에서는 불안정한 결과를 보였습니다.

---

## 🖼️ Representative Grad-CAM Examples

<div align="center">
  (Good 클래스 대표 이미지)
</div>

<br/>

<div align="center">
  (Partial 클래스 대표 이미지)
</div>

<br/>

<div align="center">
  (Poor 클래스 대표 이미지)
</div>

---

# Clinical Perspective

This system is designed to simulate how AI-based screening could be integrated into real-world clinical workflows.

본 시스템은 실제 의료 환경에서 AI 기반 스크리닝이 어떻게 활용될 수 있는지를 가정하여 설계되었습니다.

---

## 🏥 Workflow

1. **Fundus Image Capture**  
   → 안저 카메라를 통해 환자의 망막 이미지 획득  

2. **Image Upload**  
   → 병원 시스템 또는 플랫폼에 이미지 업로드  

3. **AI Analysis**  
   → 딥러닝 모델이 이미지를 분석  

4. **Disease Prediction & Risk Assessment**  
   → Top-3 질환 예측 및 위험도 제공  

5. **Explainable AI (Grad-CAM)**  
   → 모델의 판단 근거 시각화  

6. **Doctor Review**  
   → 의료진이 AI 결과를 참고하여 최종 판단  

---

<div align="center">
  (여기에 병원 사용 시나리오 흐름도 이미지 넣는 곳)
</div>

---

### 💡 Insight

The system is not intended to replace clinicians, but to **assist decision-making by prioritizing high-risk cases and providing interpretable evidence**.

본 시스템은 의료진을 대체하는 것이 아니라,  
고위험 환자를 선별하고 판단 근거를 제공하여 진단을 보조하는 역할을 수행합니다.

---

# Future Work & Limitations

## ⚠️ Limitations

- This project is intended for **research and educational purposes only**  
- The system is **not a certified medical device**  
- Performance may vary across datasets and real-world conditions  
- Some classes show lower reliability due to subtle or ambiguous features  

본 프로젝트는 연구 및 학습 목적의 시스템이며,  
의료 기기로 인증된 모델이 아니므로 실제 진단을 대체할 수 없습니다.

---

## 🚀 Future Work

- Expand dataset through real clinical data collection  
- Improve performance for underrepresented classes  
- Enhance model interpretability with advanced methods  
- Optimize model for real-time deployment  
- Integrate into clinical decision support systems  

향후에는 데이터 확장, 성능 개선, 실시간 시스템 구축 등을 통해  
실제 의료 환경에서 활용 가능한 수준으로 발전시키는 것을 목표로 합니다.

---

# Repository Structure

The repository is organized to reflect the full pipeline from data analysis to model deployment.

본 레포지토리는 데이터 분석부터 모델 학습, 그리고 데모 구현까지의 전체 흐름을 반영하여 구성되어 있습니다.

```
eye-disease-ai-screening
│
├ README.md # Project documentation
│
├ figures # Visualizations used in README
│ ├ system_architecture.png
│ ├ confusion_matrix_A.png
│ ├ confusion_matrix_B.png
│ ├ gradcam_example.png
│ └ eda_visualizations.png
│
├ notebooks # Experiment and analysis notebooks
│ ├ 01_EDA.ipynb # Data analysis & visualization
│ ├ 02_training.ipynb # Model training pipeline
│ └ 03_experiments.ipynb # Strategy comparison (A/B)
│
├ src # Core implementation
│ ├ dataset.py # Data loading & preprocessing
│ ├ model.py # Model architecture definition
│ ├ train.py # Training logic
│ └ inference.py # Inference & evaluation
│
└ demo # Deployment (Gradio app)
└ app.py # Interactive demo interface
```

### 💡 Summary

- **notebooks** → 데이터 분석 및 실험  
- **src** → 모델 구현 및 학습 코드  
- **figures** → README 시각화 자료  
- **demo** → 실제 사용자 체험을 위한 서비스  

→ 데이터 분석부터 모델 개발, 그리고 배포까지 전체 파이프라인을 포함한 프로젝트 구조입니다.
