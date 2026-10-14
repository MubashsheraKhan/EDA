import openpyxl
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

data = pd.read_excel("Online Retail.xlsx")

print(f"Dataset Shape:{data.shape}")
print(f"Dataset Rows: {data.shape[0]}")
print(f"Dataset Columns: {data.shape[1]}")
print(data.head())

data.dtypes.to_frame("dtype")

# MISSING VALUES

missing = data.isnull().sum()
missing_report = pd.DataFrame({
  "missing_count": missing,
  "missing_percentage": (missing / len(data) * 100).round(2)
})

missing_report.sort_values("missing_percentage", ascending=False)

data.duplicated().sum()
