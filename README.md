# 🥑 Avocado Ripeness Classification using K-Means Clustering

![Project Banner](images/banner.png)

> A full-stack Machine Learning project that classifies the ripeness of avocados using unsupervised learning (K-Means). Complete with EDA, clustering logic, Flask API, frontend UI, Dockerization, and optional CI/CD integration — all in one deployable application.

---

## 📌 Problem Statement

In the food and agriculture industry, detecting the ripeness of fruits like avocados is a **real-world problem**. Most assessments are visual, subjective, and often inaccurate — leading to:

- Premature harvesting
- Reduced shelf life
- Waste and economic loss

### ❓ Can we use **data-driven clustering** to predict the ripeness of avocados?

---

## 🎯 Project Goals

✅ Use sensor-based data to classify ripeness  
✅ Apply unsupervised ML (K-Means) with no labels  
✅ Deploy a web app for real-time prediction  
✅ Dockerize for easy sharing  
✅ Host API using Flask + Render  

---

## 🛠️ Tools & Technologies

| Category           | Tools/Libraries |
|-------------------|-----------------|
| ML & Scaling       | `scikit-learn`, `KMeans`, `StandardScaler` |
| Data Handling      | `pandas`, `numpy`, `matplotlib`, `seaborn` |
| API / Backend      | `Flask`, `Flask-CORS`, `joblib`, `gunicorn` |
| UI / Frontend      | `HTML`, `CSS`, `Bootstrap` |
| Deployment         | `Docker`, `Render`, `Postman` |
| Version Control    | `Git`, `GitHub` |

---

## 🧠 Dataset Overview

The dataset was collected from a combination of physical and color-based measurements of avocados at different ripeness stages.

### 📊 Features Used:

- `firmness` – softness/hardness level  
- `hue` – color tone (spectrum)  
- `saturation`, `brightness` – color depth  
- `sound_db` – sound level when tapped  
- `weight_g`, `size_cm3` – physical properties  
- `color_category_encoded` – manually encoded color label  

All features were **numeric** and **cleaned (no missing values)** before training.

---

## 📈 Exploratory Data Analysis

We visualized patterns using heatmaps, histograms, and box plots to explore feature correlations.

### 🔍 Elbow Method to determine `k`

![Elbow Method](images/elbow_plot.png)

Optimal number of clusters: **k = 3**

---

## 🔬 Model Development

### ✅ Preprocessing

- Applied `StandardScaler` to normalize all features
- Used `OrdinalEncoder` for `color_category`

### ✅ Clustering

- Applied `KMeans(n_clusters=3)`
- Saved both the model (`kmeans_model.pkl`) and scaler (`scaler.pkl`)

### ✅ Interpretation of Clusters:

| Cluster | Meaning           |
|---------|-------------------|
| 0       | Likely **Unripe** |
| 1       | Possibly **Ripe** |
| 2       | Possibly **Overripe** |

---

## 🖥️ Web App (Flask + HTML)

A lightweight web form allows users to input avocado data and receive a ripeness prediction.

![UI Form](images/web_form.png)
![Prediction Output](images/prediction_result.png)

---

## 📽️ Demo Video

🎥 **Demo on YouTube:**  
[▶️ Click to Watch the App in Action](https://youtu.be/YOUR_VIDEO_LINK)

---

## ⚙️ Docker Deployment

### Build Image:
```bash
docker build -t avocado-kmeans-app .
