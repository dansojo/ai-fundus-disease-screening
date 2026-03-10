# AI-Based Fundus Disease Screening System

<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/3589c3de-3481-4549-bbd5-7cd6e7472ff1" />

AI-assisted retinal disease screening system using deep learning and explainable AI.

This project explores the development of an AI-assisted retinal disease screening system using fundus images.
The goal is to design a prototype system that analyzes retinal images and provides risk estimation for retinal diseases, supporting early screening and assisting medical professionals in clinical decision-making.

---

# Project Motivation

Retinal diseases such as **diabetic retinopathy**, **glaucoma**, and **retinal detachment** are major causes of vision loss worldwide.

Early detection plays a critical role in preventing permanent vision impairment. However, large-scale screening remains difficult due to limited access to ophthalmologists and diagnostic resources.

This project investigates whether deep learning models can support **early screening of retinal diseases using fundus images**.

The system is designed not as a diagnostic replacement, but as a **clinical decision support tool** that helps healthcare professionals identify potential risks more efficiently.

---

# Proposed Solution

We propose an **AI-assisted screening workflow for fundus image analysis**.

```
Fundus Image
↓
AI Model Analysis
↓
Top-3 Disease Risk Prediction
↓
Grad-CAM Visual Explanation
↓
Clinical Decision Support
```

The system provides:

* Top-3 predicted retinal diseases
* Risk score estimation
* Visual explanation highlighting image regions influencing the model prediction
* Recommendation for clinical review

---

# Dataset

Dataset used: **Eye Disease Image Dataset**

Total images: **21,577**

* Original images: 5,335
* Augmented images: 16,242

Number of classes: **10**

Classes:

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

The dataset includes images collected from medical institutions in Bangladesh.

---

# Exploratory Data Analysis

EDA was performed to understand dataset characteristics.

Key observations:

* Significant **class imbalance** across disease categories
* Variations in **illumination and color distribution**
* Presence of **dataset-level augmentation**

EDA included:

* Class distribution analysis
* RGB channel statistics
* Image quality inspection

Example visualization:

```
figures/dataset_distribution.png
```

---

# System Optimization

During early experiments, **data loading performance became a bottleneck** when training in Google Colab due to Google Drive I/O latency.

To address this issue:

* Dataset **caching** was implemented
* Images were resized and stored locally
* **Throughput benchmarking** was conducted
* DataLoader parameters were optimized

These steps significantly improved training efficiency and enabled stable experimentation.

---

# Model Selection

Baseline model used in this project:

**ConvNeXtV2 Tiny**

Reasons for selection:

* Modern convolutional architecture with strong performance
* Efficient training and inference
* Suitable for limited GPU environments

Transfer learning was applied using **ImageNet pretrained weights**.

---

# Experiment Design

A major challenge identified in the dataset was **class imbalance**.

Two strategies were explored.

### Experiment A

Class Weight + Focal Loss

### Experiment B

Oversampling + Focal Loss

The goal was to determine which approach produced more stable results and better macro-level performance.

---

# Results

Evaluation metrics:

* Macro Precision
* Macro Recall
* Macro F1 Score

Baseline experiments achieved approximately:

**Macro F1 ≈ 0.90**

Experiment results showed that:

**Class Weight + Focal Loss produced more stable performance compared to Oversampling.**

Example visualization:

```
figures/confusion_matrix.png
```

---

# Explainable AI

To improve interpretability, **Grad-CAM** was implemented.

Grad-CAM highlights image regions that most influenced the model's prediction.

The system provides three visual outputs:

1. Original fundus image
2. Grad-CAM heatmap
3. Overlay visualization

This allows medical professionals to understand **why the model produced a specific prediction**.

Example:

```
figures/gradcam_example.png
```

---

# Interactive Demo

An interactive demo was implemented using **Gradio**.

The demo allows users to:

* Upload fundus images
* Receive **Top-3 disease predictions**
* View **risk scores**
* Visualize **Grad-CAM explanations**

Example workflow:

```
Upload Image
↓
AI Analysis
↓
Prediction + Explanation
```

---

# System Architecture

Example system workflow:

```
Fundus Camera
↓
Hospital System
↓
AI Screening Model
↓
Prediction + Risk Score
↓
Doctor Review
```

The AI system **assists medical professionals but does not replace clinical diagnosis**.

Example architecture diagram:

```
figures/system_architecture.png
```

---

# Future Work

Potential future directions include:

* Expanding the dataset through **hospital collaboration**
* Improving model robustness with additional training data
* Developing **real-time screening systems**
* Integrating the system into **clinical diagnostic workflows**

As more data becomes available, the model can continuously improve through retraining.

---

# Limitations

This project is intended for **research and educational purposes only**.

The system is **not a medical device** and should not be used as a substitute for professional medical diagnosis.

---

# Conclusion

This project demonstrates the feasibility of using deep learning models to assist retinal disease screening using fundus images.

Beyond model development, the project explores how such systems could be integrated into **real-world clinical workflows through explainable AI and interactive interfaces**.

The work highlights the potential of AI-assisted screening systems to support healthcare professionals and improve early detection of retinal diseases.
