# ❤️ Heart Disease Data Cleaning & Preprocessing (EDA)

A complete data cleaning and preprocessing project on the Heart Disease dataset using **Python, Pandas, NumPy, and Scikit-learn**. This notebook prepares the dataset for Exploratory Data Analysis (EDA) and Machine Learning by handling categorical variables, feature engineering, correlation analysis, and data validation.

---

## 📌 Project Overview

This project focuses on cleaning and transforming the Heart Disease dataset into a machine learning–ready format.

**Dataset Summary**

- **Rows:** 918
- **Original Columns:** 12
- **Final Columns after Encoding:** 18
- **Target Variable:** `HeartDisease`

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
Heart-Disease-EDA/
│
├── data/
│   └── heart.csv
│
├── notebooks/
│   └── Project2.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧹 Data Cleaning Steps Performed

### 1. Dataset Inspection

- Loaded dataset using Pandas.
- Checked dataset shape.
- Inspected data types with `info()`.
- Generated summary statistics using `describe()`.

### 2. Missing Value Check

- Verified missing values using `isnull().sum()`.
- Dataset contains **no missing values**.

### 3. Duplicate Removal

- Checked duplicate rows using `duplicated().sum()`.
- Removed duplicates if present.

### 4. Categorical Encoding

#### Label Encoding

Applied Label Encoding on binary categorical columns:

- `Sex`
- `ExerciseAngina`

#### One-Hot Encoding

Applied One-Hot Encoding on multi-category columns:

- `ChestPainType`
- `RestingECG`
- `ST_Slope`

### 5. Feature Engineering

Created age groups using `pd.cut()`:

- Young
- Middle Aged
- Elderly

Converted the new age category into dummy variables using One-Hot Encoding.

### 6. Correlation Analysis

Performed Pearson Correlation to understand relationships between numerical features and the target variable (`HeartDisease`).

### 7. Data Validation

Final verification included:

- No missing values.
- No duplicate records.
- All categorical columns converted to numerical format.
- Dataset ready for EDA and ML.

---

## 📊 Features in the Cleaned Dataset

| Feature Type | Columns |
|--------------|---------|
| Numerical | Age, RestingBP, Cholesterol, MaxHR, Oldpeak |
| Binary Encoded | Sex, ExerciseAngina, FastingBS, HeartDisease |
| One-Hot Encoded | ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_Normal, RestingECG_ST, ST_Slope_Flat, ST_Slope_Up |
| Engineered Features | Age_Category_Middle_Aged, Age_Category_Elderly |

---

## 📈 Pearson Correlation

Pearson Correlation was used to measure the **strength and direction of the linear relationship** between numerical features and the target variable.

Key observations:

- `ST_Slope_Up` shows a strong negative correlation with heart disease.
- `ST_Slope_Flat` and `ExerciseAngina` show strong positive correlations.
- `Oldpeak`, `Age`, and `FastingBS` also have meaningful relationships with the target.

---

## ✅ Outcome

The dataset is fully cleaned and transformed for the next stage of the data science workflow:

- Exploratory Data Analysis (EDA)
- Feature Scaling
- Train-Test Split
- Machine Learning Model Building

---

## 🚀 Future Work

- Perform Univariate and Bivariate EDA.
- Visualize feature distributions and outliers.
- Apply Feature Scaling.
- Train classification models such as Logistic Regression, Decision Tree, Random Forest, SVM, and XGBoost.
- Evaluate model performance using accuracy, precision, recall, F1-score, and ROC-AUC.

---

## 📚 Learning Objective

This project was completed as part of learning **Exploratory Data Analysis (EDA)** and **Machine Learning preprocessing** in a Data Science workflow using Python.
