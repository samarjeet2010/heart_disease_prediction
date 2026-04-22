# ❤️ Heart Disease Prediction ML Project

## 📌 Overview

This project is a **Machine Learning-based Heart Disease Prediction System** that predicts whether a person is at risk of heart disease based on medical parameters.

It uses multiple ML models and provides prediction along with model accuracy.

---

## 🚀 Features

* Predicts heart disease risk (Yes/No)
* User-friendly web interface
* Multiple ML models used:

  * 🌳 Random Forest
  * 📈 Logistic Regression
  * ⚡ Gradient Boosting
* Displays model accuracy
* Fast API integration with frontend

---

## 🖥️ Project Structure

```
heart_project/
│── index.html        # Frontend UI
│── app.py            # Backend (API)
│── model files       # Trained ML models
│── dataset.csv       # Dataset (if included)
```

---

## 🧠 Input Parameters

The model takes the following inputs:

* Age
* Sex (0 = Female, 1 = Male)
* Chest Pain Type
* Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Rest ECG
* Maximum Heart Rate
* Exercise Induced Angina
* Oldpeak

---

## ⚙️ Technologies Used

* Python 🐍
* Scikit-learn
* Pandas & NumPy
* HTML, CSS, JavaScript
* FastAPI / Flask (Backend API)

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run backend server

```
python app.py
```

### 4. Open frontend

* Open `index.html` in browser

---

## 🔗 API Endpoint

```
POST http://127.0.0.1:8000/predict
```

---

## 📊 Output

* ✅ No Heart Disease
* ⚠️ Heart Disease Risk

Also shows:

* Random Forest Accuracy
* Logistic Regression Accuracy
* Gradient Boosting Accuracy

---

## 📸 UI Preview

Simple web interface where users input medical data and get instant prediction.
## 📸 UI Preview

Simple web interface where users input medical data and get instant prediction.

![Heart Disease UI Preview](input.png)

![Heart Disease UI Preview](output.png)

---
---



---

## 👨‍💻 Author

**Samar Jeet**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
