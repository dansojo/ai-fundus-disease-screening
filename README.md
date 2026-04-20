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

본 프로젝트는 실제 병원에서 수집된 안저 이미지 데이터셋을 활용합니다.

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
  (여기에 클래스별 데이터 분포 그래프 이미지 넣는 곳)
</div>

---

### 🖼️ Sample Images

<div align="center">
  (여기에 클래스별 샘플 이미지 예시 넣는 곳)
</div>

---

## 🔍 Exploratory Data Analysis

EDA was conducted to understand dataset characteristics and identify potential challenges affecting model performance.

데이터의 특성과 학습에 영향을 줄 수 있는 요소를 파악하기 위해 EDA를 수행했습니다.

---

### ⚠️ Key Observations

- **Severe class imbalance exists across disease categories**  
- **Image brightness and quality vary significantly**  
- **Augmented images are included and may affect distribution**

---

### 📊 Class Imbalance

<div align="center">
  (여기에 클래스 불균형 그래프 이미지 넣는 곳)
</div>

---

### 🎨 RGB Channel Analysis

<div align="center">
  (여기에 RGB 채널 분석 시각화 이미지 넣는 곳)
</div>

---

### 📐 Image Resolution Analysis

<div align="center">
  (여기에 이미지 해상도 분석 그래프 넣는 곳)
</div>

---

### 💡 Summary

- 데이터셋은 클래스 간 불균형이 심하게 존재함  
- 이미지 품질(밝기, 대비)이 일정하지 않음  
- 증강 데이터가 포함되어 있어 분포 왜곡 가능성 존재  

→ 이러한 특성은 모델 학습 및 일반화 성능에 직접적인 영향을 미칠 수 있음

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
  (여기에 ConvNeXt 구조 설명 이미지 넣는 곳)
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
  (여기에 실험 구조 다이어그램 넣는 곳)
</div>

---

### 💡 Summary

- Class imbalance was the primary challenge in this dataset  
- Two complementary strategies were tested to address it  
- These approaches are further compared in the Results section

---

# Results

Evaluation metrics

* Accuracy
* Precision
* Recall
* Macro F1 Score

Best result

Macro F1 ≈ 0.90

(여기에 **실험 결과 비교 표 이미지 넣을 자리**)

(여기에 **A/B 실험 성능 비교 그래프 넣을 자리**)

---

# Confusion Matrix

The confusion matrix was used to analyze the model's prediction behavior across all classes.

To better understand class-wise performance and misclassification patterns, **row-normalized confusion matrices** were used instead of raw count matrices.

---

## Comparison of Training Strategies

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

## Key Observations

- Most classes show strong classification performance with high diagonal dominance.
- Several classes (e.g., Class 1, 2, 7, 8, 9) are classified almost perfectly, indicating clear and distinguishable visual patterns.

---

### Confusion Patterns

- Misclassification mainly occurs among visually similar classes.
- Notable confusion is observed between:
  - Class 3 ↔ Class 4
  - Class 3 ↔ Class 5
  - Class 6 ↔ Class 3

This suggests that the model struggles to distinguish diseases with **similar lesion locations and visual characteristics**, particularly around the macular region.

---

### Strategy Comparison

- **Class Weight + Focal Loss (A)** shows more stable and consistent performance across classes.
- **Oversampling + Focal Loss (B)** slightly increases misclassification in certain classes.

This is likely due to:
- Repeated samples in oversampling
- Increased risk of overfitting
- Introduction of noise in minority classes

---

## Final Insight

Although both strategies achieve strong overall performance,  
**Class Weighting provides a better balance between stability and generalization.**

Oversampling helps address class imbalance but may introduce unintended bias and noise.

---

## Conclusion

The confusion matrix analysis reveals that:

- The model performs well on most classes
- Performance degradation occurs primarily between visually similar diseases
- Careful handling of class imbalance is critical for stable learning

These findings are consistent with Grad-CAM analysis, where the model tends to focus on overlapping anatomical regions across similar disease categories.

---

# Explainable AI

To improve model interpretability, **Grad-CAM** was applied to visualize the image regions that influenced model predictions.

This allows us to verify whether the model focuses on clinically relevant regions rather than relying on irrelevant patterns.

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

Glaucoma is associated with structural changes in the optic disc, such as an increased cup-to-disc ratio.

The Grad-CAM visualization shows that the model consistently attends to the optic disc region, which aligns with clinically relevant features.  
However, in some cases, attention is spread beyond the target region, indicating that the model has not fully learned fine-grained structural characteristics.

---

# Class-wise Model Reliability Analysis

Based on Grad-CAM visualization, we analyzed how reliably the model identifies disease-specific features for each class.

We categorized the model behavior into three levels:

🟢 Good (Reliable)
* Diabetic Retinopathy
* Retinitis Pigmentosa
* Glaucoma

→ The model consistently focused on clinically meaningful lesion regions.

🟡 Partial (Unstable)
* Macular Scar
* Central Serous Chorioretinopathy
* Disc Edema
* Retinal Detachment

→ The model partially captured lesion areas but showed inconsistent or biased attention patterns.

🔴 Poor (Unreliable)
* Pterygium
* Myopia
* Healthy

→ The model failed to identify meaningful features or relied on irrelevant regions.

## Key Insight

The analysis reveals that model performance is not uniform across classes.
Some diseases with strong visual patterns are well learned, while others with weak or ambiguous features are not reliably captured.

This highlights the importance of class-wise evaluation beyond overall accuracy metrics.

Representative Grad-CAM Examples

(여기에 Good 클래스 대표 Grad-CAM 이미지 1장 넣는 곳)

(여기에 Partial 클래스 대표 Grad-CAM 이미지 1장 넣는 곳)

(여기에 Poor 클래스 대표 Grad-CAM 이미지 1장 넣는 곳)

---

# Potential Clinical Workflow

Possible usage in a clinical environment

Fundus camera captures retinal image
↓
Image uploaded to hospital system
↓
AI model analyzes image
↓
Disease risk score generated
↓
Doctor reviews AI suggestion

(여기에 **병원 실제 사용 시나리오 흐름도 이미지 넣을 자리**)

---

# Future Improvements

Possible improvements

* Expand dataset through hospital collaboration
* Improve model performance with additional data
* Deploy real-time clinical screening systems
* Integrate into hospital diagnostic workflows

---

# Limitations

This project is intended for **research and educational purposes only**.

The system is not a certified medical device and should not replace professional medical diagnosis.

---

# Repository Structure

```
eye-disease-ai-screening
│
├ README.md
│
├ figures
│   ├ system_architecture.png
│   ├ confusion_matrix.png
│   └ gradcam_example.png
│
├ notebooks
│   ├ 01_EDA.ipynb
│   ├ 02_training.ipynb
│   └ 03_experiments.ipynb
│
├ src
│   ├ dataset.py
│   ├ model.py
│   ├ train.py
│   └ inference.py
│
└ demo
    └ gradio_app.py
```
