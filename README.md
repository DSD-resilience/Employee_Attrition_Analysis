# 🧑‍💼 Employee Attrition Analysis

This project performs data cleaning and basic exploratory data analysis (EDA) on an HR dataset to understand the patterns and insights behind employee attrition. 
It's a simple but practical Python script showcasing foundational data analysis skills.

---

## 📂 Dataset

- **Name**: IBM HR Analytics Employee Attrition & Performance
- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **File Used**: `WA_Fn-UseC_-HR-Employee-Attrition.csv`

---

## 🔍 What the Script Does

### 1. Data Cleaning
- Removes unnecessary or redundant columns
- Converts selected columns to appropriate data types
- Handles missing data (if any)

### 2. Exploratory Data Analysis (EDA)
- Summary statistics and data overview
- Attrition rates by department and job role
- Comparison of age and salary between employees who stayed and those who left

### 3. Visualizations
- Bar chart of attrition distribution
- Histogram of age by attrition status
- Boxplot of monthly income vs attrition

Charts are saved as PNG files in the working directory.

---

## 📁 Files in This Repo

| File Name                        | Description                                 |
|----------------------------------|---------------------------------------------|
| `employee_attrition_analysis.py`| Main Python script                          |
| `WA_Fn-UseC_-HR-Employee-Attrition.csv` | Dataset file                            |
| `cleaned_employee_data.csv`     | Cleaned version of the dataset (output)     |
| `attrition_count.png`           | Bar chart of attrition                     |
| `age_distribution.png`          | Age histogram by attrition                 |
| `income_boxplot.png`            | Monthly income vs attrition boxplot        |

---

## 🛠 Requirements

Install dependencies with:

```bash
pip install pandas matplotlib seaborn
