# 🏡 House Price Predictor

This project is a complete end-to-end machine learning pipeline for predicting house prices based on property features — from exploratory data analysis to a real-time web application.

Built with **Python**, **Flask**, and **scikit-learn**, the app allows users to input housing details through a friendly interface and instantly receive a price prediction.

---

## 🚀 Demo Preview

### 🧾 Input Form
<img src="images/form.PNG" alt="Input form" width="400"/>

### 📈 Prediction Output
<img src="images/result.PNG" alt="Prediction result" width="300"/>

---

## 🧠 Project Purpose

This project was developed as part of my learning journey to:
- 🔍 Practice real-world data analysis (EDA)
- 🤖 Apply and compare regression models
- 🌐 Build a user-facing ML application with Flask
- 💡 Stay motivated by turning notebooks into working tools


---

## 🧱 Full Tech Stack

### 🖥️ Backend
- **Python** – Core programming language  
- **Flask** – Web framework for routing and rendering  
- **joblib** – Load the trained model (`model.pkl`)  
- **pandas** – Prepare and format input features

### 🤖 Machine Learning
- **scikit-learn** – For:
  - Training: **Linear**, **Ridge**, **Lasso**
  - Evaluation & preprocessing  
- **xgboost** – For **XGBoost Regressor**
- **joblib** – For saving and loading the trained model

### 📊 Data Analysis & Preprocessing
- **pandas**, **numpy**, **missingno** – Cleaning and null analysis  
- **matplotlib**, **seaborn** – Visualizations and plots

### 🎨 Frontend
- **HTML5 + CSS3** – Form and output pages  
- **Jinja2** – HTML rendering via Flask  
- **Emoji icons** – User-friendly form elements

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app
```bash
python app.py
```

### 4. Open in your browser
```
http://localhost:5000
```

---

## 🧪 Model Overview

This project compares and evaluates multiple regression models:
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- XGBoost Regressor  

✅ The best-performing model was saved as `model.pkl` and is used in the live app.

---

## 📌 Evaluation Metrics
- R² Score  
- Mean Squared Error (MSE)  
- Actual vs. Predicted plots  

📎 _Note: `SalePrice` was log-transformed during training for better model accuracy._

---

## 📂 Project Structure
```
## 📂 Project Structure

```text
house-price-predictor/
│
├── app.py                       # Flask web application
├── form.html                    # HTML file 
├── Dockerfile                   # Docker setup for containerization
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
│
├── EDA_to_model.ipynb           # Main notebook: EDA and model training
│
├── data/                        # Raw dataset files
│   ├── train.csv
│   └── test.csv
│
├── images/                      # UI screenshots for README
│   ├── form.PNG
│   └── result.PNG
│
├── models/                      # Trained model files
│   ├── model.pkl
│   └── xgb_best_pipeline.pkl
│
└──  notebooks/                   # (Empty or for future notebooks)

```

---

## 👩‍💻 Author

**Manal Babkhouti**  
Engineering Student | Learning ML & Data Apps  
🛠️ Turning code into real tools, one project at a time.


