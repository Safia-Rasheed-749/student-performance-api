# 🎓 Student Performance Prediction System

An end-to-end machine learning project that predicts a student's overall performance based on study habits, subject scores, and background factors. Built with a client-server architecture using FastAPI (backend) and Streamlit (frontend).

---

## 🌐 Live Demo

- **Frontend (Streamlit):** [Student Performance Predictor](https://student-performance-api-weeugym95dss7magahkegd.streamlit.app/)
- **Backend API (Render):** [FastAPI Docs](https://student-performance-api-b8wn.onrender.com/docs)
- **Health Check:** [API Health](https://student-performance-api-b8wn.onrender.com/health)

---

## 📊 Project Overview

| Component | Technology | Deployment |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Streamlit Community Cloud |
| **Backend API** | FastAPI | Render (Free Tier (Hobby Plan)) |
| **Model** | Linear Regression | Pickle (saved) |
| **Language** | Python 3.11 | - |

---

## 🧠 Model Performance

| Metric | Score |
| :--- | :--- |
| **R² Score** | **93.74%** |
| **Mean Absolute Error (MAE)** | 3.81 |
| **Root Mean Squared Error (RMSE)** | 4.77 |
| **Overfitting Check** | ✅ No overfitting (Train/Test gap < 0.01) |

---

---

## 🚀 Features

- **4-Step User Input Flow:** Study Habits → Subject Scores → Background → Predict
- **Dynamic Confidence Score:** Color-coded (🟢 High / 🟡 Medium / 🔴 Low)
- **Real-time Predictions:** via FastAPI backend
- **Production-Ready Architecture:** Decoupled frontend and backend

---

## 🛠️ How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/Safia-Rasheed-749/student-performance-api.git
2. Backend (FastAPI)
pip install -r requirements.txt
uvicorn app.main:app --reload
→ API available at: http://localhost:8000

3. Frontend (Streamlit)
cd student_performance_frontend
pip install -r requirements.txt
streamlit run app.py
→ App available at: http://localhost:8501

student_performance_api(main folder) has backend file plus 2 folders:
1. student_performance_frontend(having frontend code)
2. Student_Performance_Project(having train_mode.py, dataset file and .pkl files(saved model &preprocessor))

📊 Dataset
https://www.kaggle.com/datasets/kundanbedmutha/student-performance-dataset

👩‍💻 Author
Safia Rasheed
GitHub: @Safia-Rasheed-749
This project is for educational purposes as part of an ML course assignment.
⭐ If you find this project useful, please consider giving it a star!




