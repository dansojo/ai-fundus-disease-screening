# AI-Based Fundus Disease Screening System

---

# Project Overview

Retinal diseases such as diabetic retinopathy, glaucoma, and retinal detachment are major causes of vision loss worldwide.

Early detection plays a critical role in preventing permanent damage. However, large-scale screening remains challenging due to the limited number of specialists.

This project explores an **AI-assisted retinal disease screening system** that analyzes fundus images and predicts potential diseases while providing visual explanations to support medical professionals.

---

# System Architecture

<img width="1264" height="842" alt="Image" src="https://github.com/user-attachments/assets/34a225aa-c58d-43b5-9e2a-fbebbeacc462" />

Workflow

Fundus Image Capture

↓

Hospital System / Upload

↓

AI Screening Model

↓

Top-3 Disease Prediction

↓

Explainable AI (GradCAM)

↓

Risk Score Assessment

↓

Doctor Review

---

# Problem Statement

Retinal diseases require early detection, but large-scale screening is difficult in many healthcare environments.

AI-assisted screening systems can support clinicians by identifying high-risk cases and prioritizing further medical examination.

This project focuses on designing a **screening-support AI system**, not a replacement for medical diagnosis.

---

# Dataset

Dataset used: **Eye Disease Image Dataset**

Source Hospitals

* Anwara Hamida Eye Hospital
* BNS Zahrul Haque Eye Hospital
* Bangladesh

Dataset statistics

Total images: **21,577**

Original images: **5,335**
Augmented images: **16,242**

Number of classes: **10**

(여기에 **클래스별 데이터 분포 그래프 이미지 넣을 자리**)

(여기에 **클래스별 샘플 이미지 예시 넣을 자리**)

Disease classes include

* Central Serous Chorioretinopathy
* Diabetic Retinopathy
* Disc Edema
* Glaucoma
* Healthy
* Macular Scar
* Myopia
* Pterygium
* Retinal Detachment
* Retinitis Pigmentosa

---

# Exploratory Data Analysis

EDA was conducted to understand dataset characteristics.

Key observations

* Dataset includes strong **class imbalance**
* Image brightness and quality vary
* Augmented images are included in the dataset

(여기에 **클래스 불균형 그래프 이미지 넣을 자리**)

(여기에 **RGB 채널 분석 시각화 이미지 넣을 자리**)

(여기에 **이미지 해상도 분석 그래프 넣을 자리**)

---

# Model Development

Model architecture

ConvNeXtV2 Tiny

Framework

PyTorch

Training strategy

Transfer learning with pretrained ImageNet weights.

Training configuration

Image size: 224 × 224
Optimizer: AdamW
Scheduler: CosineAnnealingLR
Mixed Precision Training (AMP)

(여기에 **모델 구조 설명 이미지 넣을 자리 (ConvNeXt 구조)**)

---

# Experiment Design

Class imbalance was identified as the main challenge.

Two strategies were tested.

### Experiment A

Class Weight + Focal Loss

Purpose

Reduce bias toward majority classes and focus learning on difficult samples.

### Experiment B

Oversampling + Focal Loss

Purpose

Increase minority class representation during training.

(여기에 **실험 구조 설명 다이어그램 넣을 자리**)

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
      <img src="figures/system_architecture.png" width="800"/>
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
