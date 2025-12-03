# employee_attrition_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# 1. Load Dataset
# ------------------------------
# Replace with your dataset path if needed
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# ------------------------------
# 2. Initial Data Check
# ------------------------------
print("Initial Dataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nBasic Stats:")
print(df.describe())

# ------------------------------
# 3. Data Cleaning
# ------------------------------
# Drop columns that do not add value
columns_to_drop = ['EmployeeNumber', 'EmployeeCount', 'Over18', 'StandardHours']
df.drop(columns=columns_to_drop, axis=1, inplace=True)

# Convert some columns to category
categorical_cols = ['Attrition', 'BusinessTravel', 'Department', 'EducationField', 'Gender',
                    'JobRole', 'MaritalStatus', 'OverTime']
for col in categorical_cols:
    df[col] = df[col].astype('category')

# ------------------------------
# 4. Basic EDA
# ------------------------------
print("\nAttrition Value Counts:")
print(df['Attrition'].value_counts())

# Compare attrition rates by Job Role
print("\nAttrition Rate by Job Role:")
print(df.groupby('JobRole')['Attrition'].value_counts(normalize=True).unstack().fillna(0))

# Average age and income comparison
print("\nAverage Age by Attrition:")
print(df.groupby('Attrition')['Age'].mean())

print("\nAverage Monthly Income by Attrition:")
print(df.groupby('Attrition')['MonthlyIncome'].mean())

# ------------------------------
# 5. Visualizations
# ------------------------------

# Set theme
sns.set(style="whitegrid")

# Attrition count plot
plt.figure(figsize=(6, 4))
sns.countplot(x='Attrition', data=df)
plt.title("Employee Attrition Count")
plt.savefig("attrition_count.png")
plt.close()

# Histogram of age
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Age', hue='Attrition', multiple='stack', bins=20)
plt.title("Age Distribution by Attrition")
plt.savefig("age_distribution.png")
plt.close()

# Boxplot: Monthly Income vs Attrition
plt.figure(figsize=(8, 5))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title("Monthly Income by Attrition")
plt.savefig("income_boxplot.png")
plt.close()

print("EDA completed. Charts saved as PNG files.")

# ------------------------------
# 6. (Optional) Save cleaned dataset
# ------------------------------
df.to_csv("cleaned_employee_data.csv", index=False)
