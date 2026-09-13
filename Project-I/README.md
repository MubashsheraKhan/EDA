# 💰 Insurance Charges Data Cleaning & Exploratory Data Analysis (EDA)

A complete data cleaning and exploratory data analysis project on the Medical Insurance Charges dataset using **Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn**.

This project focuses on understanding the factors that influence insurance charges through data cleaning, visualization, feature engineering, and correlation analysis.

---

## 📌 Project Overview

This notebook performs EDA on a medical insurance dataset and prepares it for future machine learning models.

### Dataset Summary

- **Rows:** 1,338
- **Columns:** 7
- **Target Variable:** `charges`

### Features

| Feature | Type |
|---------|------|
| age | Integer |
| sex | Categorical |
| bmi | Float |
| children | Integer |
| smoker | Categorical |
| region | Categorical |
| charges | Float (Target) |

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📂 Project Structure

```
Insurance-Charges-EDA/
│
├── data/
│   └── insurance.csv
│
├── notebooks/
│   └── Project1.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧹 Data Cleaning Steps Performed

### 1. Dataset Inspection

- Loaded dataset using Pandas.
- Checked shape, data types, and summary statistics.

### 2. Missing Value Analysis

- Verified missing values using `isnull().sum()`.
- Confirmed the dataset contains no missing values.

### 3. Duplicate Check

- Checked duplicate records.
- Removed duplicates if present.

### 4. Categorical Encoding

Encoded categorical columns into numerical format:

- `sex`
- `smoker`
- `region`

### 5. Correlation Analysis

Applied Pearson Correlation to identify relationships between numerical features and insurance charges.

### 6. Data Validation

Verified:

- No missing values.
- No duplicate rows.
- Correct data types after preprocessing.

---

## 📊 Exploratory Data Analysis

The notebook includes:

- Distribution analysis of numerical features.
- Categorical feature analysis.
- Correlation heatmap.
- Relationship between features and insurance charges.

---

## 📈 Key Insights

Some important patterns explored in this project include:

- Effect of smoking on insurance charges.
- Relationship between BMI and charges.
- Age vs insurance charges.
- Regional distribution of customers.
- Impact of number of children on charges.

---

## ✅ Outcome

The dataset is cleaned and prepared for the next stage of the data science workflow:

- Feature Scaling
- Train-Test Split
- Regression Model Building
- Model Evaluation

---

## 🚀 Future Work

- Apply StandardScaler and MinMaxScaler.
- Build regression models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor
- Evaluate using MAE, MSE, RMSE, and R² Score.

---

## 👩‍💻 Author

**Mubashshera Khan**
