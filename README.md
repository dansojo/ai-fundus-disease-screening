# AI-Based Fundus Disease Screening System

---

# Project Overview

Retinal diseases such as diabetic retinopathy, glaucoma, and retinal detachment are major causes of vision loss worldwide.

Early detection plays a critical role in preventing permanent damage. However, large-scale screening remains challenging due to the limited number of specialists.

This project explores an **AI-assisted retinal disease screening system** that analyzes fundus images and predicts potential diseases while providing visual explanations to support medical professionals.

---

# System Architecture

(여기에 **전체 서비스 구조 설명 아키텍처 이미지** 삽입)

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

The confusion matrix shows model prediction performance across all classes.

![Confusion Matrix](figures/confusion_matrix.png)

(여기에 **Confusion Matrix 이미지 삽입**)

---

# Explainable AI

To improve model interpretability, **GradCAM** was applied.

GradCAM visualizes the image regions that influenced model predictions.

This helps medical professionals understand why the model made a specific prediction.

(여기에 **GradCAM 예시 이미지 넣을 자리**)

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
