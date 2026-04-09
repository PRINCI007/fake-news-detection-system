# 📰 Fake News Detection System

A full-stack machine learning project that classifies news articles as **Fake** or **Real** using Natural Language Processing and a microservices-based architecture.

---

## 🚀 Features

* 🔍 Detects whether news content is Fake or Real
* ⚡ Real-time prediction using REST API
* 🧠 Machine Learning model with ~98% accuracy
* 🔗 Integration of Python (Flask) with Java (Spring Boot)
* 🎨 Simple and interactive frontend interface

---

## 🏗️ Tech Stack

### 🔹 Machine Learning

* Python
* Pandas, NumPy
* Scikit-learn (TF-IDF, Logistic Regression)

### 🔹 Backend

* Java
* Spring Boot
* REST APIs

### 🔹 Frontend

* HTML
* CSS
* JavaScript

---

## ⚙️ System Architecture

Frontend -> Spring Boot -> Flask API -> ML Model -> Response

---

## 📂 Project Structure

fake-news-detection-system/<br>
|<br>
├── backend-springboot/<br>
├── frontend/<br>
├── ml-model/<br>
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Run Machine Learning API (Flask)

cd ml-model
python app.py

Runs on:
http://127.0.0.1:5000

---

### 2️⃣ Run Spring Boot Backend

* Open `backend-springboot` in IntelliJ IDEA
* Run the application

Runs on:
http://localhost:8080

---

### 3️⃣ Run Frontend

* Open `frontend/index.html` in your browser

---

## 🧪 API Endpoint

### POST Request

http://localhost:8080/api/news/predict

### Request Body

{
"text": "Enter your news text here"
}

### Response

{
"prediction": "Real",
"confidence": "95.23%"
}

---

## 📊 Model Details

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF
* Accuracy: ~98%
* Dataset: Fake and Real news dataset

---

## ⚠️ Limitations

* Works best with structured news articles
* Short or vague inputs may produce low-confidence results

---

## 👩‍💻 Author

**Princi Sharma**

GitHub: https://github.com/PRINCI007
LinkedIn: https://linkedin.com/in/princi-sharma-4269aa340

---

## ⭐ Future Scope

* Improve model accuracy with advanced NLP techniques
* Add uncertainty handling
* Enhance UI/UX design
* Deploy the project online

---

## 📌 Note

This project demonstrates the integration of Machine Learning with a full-stack web application using a microservices architecture.
