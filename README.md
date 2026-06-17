# 🩺 Health Prediction Application

A web-based healthcare application built using **Python**, **Streamlit**, and **SQLite** for managing patient records and predicting possible health risks based on blood test results.

---

## 📌 Overview

The Health Prediction Application enables users to store, manage, update, and analyze patient health information through a simple and user-friendly interface.

The application predicts possible health risks using blood test values and automatically generates health remarks based on predefined medical thresholds.

---

## ✨ Features

### 👤 Patient Management

* Add new patient records
* View all patient records
* Update existing patient information
* Delete patient records

### ✅ Data Validation

* Full Name validation
* Email format validation
* Date of Birth validation
* Numeric input validation for blood test values

### 🧠 Health Risk Prediction

The application predicts potential health risks using:

* Glucose Level
* Haemoglobin Level
* Cholesterol Level

### 💾 Persistent Storage

* SQLite database integration
* Secure storage and retrieval of patient records

---

## 📋 Patient Information

The application stores the following information:

* Full Name
* Date of Birth
* Email Address
* Glucose
* Haemoglobin
* Cholesterol
* Remarks

---

## 🔍 Prediction Logic

The application uses a rule-based health prediction approach.

| Condition         | Prediction             |
| ----------------- | ---------------------- |
| Glucose ≥ 126     | Possible Diabetes Risk |
| Haemoglobin < 12  | Possible Anaemia       |
| Cholesterol ≥ 240 | High Cholesterol Risk  |

If no health risk is detected:

**No Significant Risk Detected**

---

## 🔄 CRUD Operations

### Create

Add new patient records to the database.

### Read

Display all patient records in a tabular format.

### Update

Modify existing patient information using Patient ID.

### Delete

Remove patient records from the database.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* SQLite
* Pandas

---

## 📂 Project Structure

```text
health-prediction-app/

├── app.py
├── database.py
├── predictor.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🚀 Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 🗄️ Database

Database: SQLite

Table: patients

Fields:

* id
* full_name
* dob
* email
* glucose
* haemoglobin
* cholesterol
* remarks

---

## 📷 Application Workflow

1. Enter patient details.
2. Validate user inputs.
3. Predict possible health risks.
4. Save patient information to the database.
5. Display all patient records.
6. Update patient records when required.
7. Delete patient records when required.

---

## 🔮 Future Enhancements

* External Health API Integration
* Machine Learning-Based Prediction Models
* Search and Filter Functionality
* Interactive Dashboard and Visualizations

---

## 👩‍💻 Author

**Alakananda P**
