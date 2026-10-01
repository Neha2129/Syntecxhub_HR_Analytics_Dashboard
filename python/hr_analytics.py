import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# 1. Load Dataset
# -----------------------------
file_path = "../Dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


# -----------------------------
# 2. Basic Information
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

print("\nAttrition Distribution:")
print(df["Attrition"].value_counts())


# -----------------------------
# 3. Create Output Folder
# -----------------------------
output_folder = "../Dataset/Analysis_Outputs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# -----------------------------
# 4. Attrition Analysis
# -----------------------------
attrition_analysis = (
    df.groupby("Department")["Attrition"]
    .value_counts()
    .unstack(fill_value=0)
)

attrition_analysis.to_csv(
    f"{output_folder}/Department_Attrition_Analysis.csv"
)

print("\nDepartment-wise Attrition:")
print(attrition_analysis)


# -----------------------------
# 5. Job Role Attrition
# -----------------------------
role_attrition = (
    df.groupby("JobRole")["Attrition"]
    .value_counts()
    .unstack(fill_value=0)
)

role_attrition.to_csv(
    f"{output_folder}/JobRole_Attrition_Analysis.csv"
)

print("\nJob Role-wise Attrition:")
print(role_attrition)


# -----------------------------
# 6. Salary Analysis
# -----------------------------
salary_analysis = (
    df.groupby("Department")["MonthlyIncome"]
    .agg(["mean", "min", "max"])
    .reset_index()
)

salary_analysis.to_csv(
    f"{output_folder}/Department_Salary_Analysis.csv",
    index=False
)

print("\nSalary Analysis:")
print(salary_analysis)


# -----------------------------
# 7. Experience Analysis
# -----------------------------
experience_analysis = (
    df.groupby("Department")["TotalWorkingYears"]
    .mean()
    .reset_index()
)

experience_analysis.columns = [
    "Department",
    "Average_Total_Working_Years"
]

experience_analysis.to_csv(
    f"{output_folder}/Department_Experience_Analysis.csv",
    index=False
)

print("\nExperience Analysis:")
print(experience_analysis)


# -----------------------------
# 8. Overtime vs Attrition
# -----------------------------
overtime_attrition = (
    pd.crosstab(
        df["OverTime"],
        df["Attrition"],
        normalize="index"
    ) * 100
)

overtime_attrition.to_csv(
    f"{output_folder}/Overtime_Attrition_Analysis.csv"
)

print("\nOvertime vs Attrition (%):")
print(overtime_attrition)


# -----------------------------
# 9. Job Satisfaction vs Attrition
# -----------------------------
satisfaction_attrition = (
    pd.crosstab(
        df["JobSatisfaction"],
        df["Attrition"],
        normalize="index"
    ) * 100
)

satisfaction_attrition.to_csv(
    f"{output_folder}/JobSatisfaction_Attrition_Analysis.csv"
)

print("\nJob Satisfaction vs Attrition (%):")
print(satisfaction_attrition)


# -----------------------------
# 10. Correlation Analysis
# -----------------------------
correlation_columns = [
    "Age",
    "DistanceFromHome",
    "JobLevel",
    "JobSatisfaction",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PerformanceRating",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "WorkLifeBalance",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]

correlation_matrix = df[correlation_columns].corr()

correlation_matrix.to_csv(
    f"{output_folder}/Correlation_Matrix.csv"
)

print("\nCorrelation Matrix:")
print(correlation_matrix)


# -----------------------------
# 11. Create Attrition Numeric Column
# -----------------------------
df["Attrition_Numeric"] = df["Attrition"].map({
    "Yes": 1,
    "No": 0
})


# -----------------------------
# 12. Correlation with Attrition
# -----------------------------
attrition_correlation_columns = correlation_columns + [
    "Attrition_Numeric"
]

attrition_correlation = (
    df[attrition_correlation_columns]
    .corr()["Attrition_Numeric"]
    .sort_values(ascending=False)
)

attrition_correlation.to_csv(
    f"{output_folder}/Attrition_Correlation.csv"
)

print("\nCorrelation with Attrition:")
print(attrition_correlation)


# -----------------------------
# 13. KPI Summary
# -----------------------------
total_employees = len(df)
attrition_count = (df["Attrition"] == "Yes").sum()
retention_count = (df["Attrition"] == "No").sum()

attrition_rate = (attrition_count / total_employees) * 100
retention_rate = (retention_count / total_employees) * 100

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Employees",
        "Attrition Count",
        "Retention Count",
        "Attrition Rate",
        "Retention Rate",
        "Average Monthly Income",
        "Average Total Working Years"
    ],
    "Value": [
        total_employees,
        attrition_count,
        retention_count,
        round(attrition_rate, 2),
        round(retention_rate, 2),
        round(df["MonthlyIncome"].mean(), 2),
        round(df["TotalWorkingYears"].mean(), 2)
    ]
})

kpi_summary.to_csv(
    f"{output_folder}/HR_KPI_Summary.csv",
    index=False
)

print("\nKPI Summary:")
print(kpi_summary)


# -----------------------------
# 14. Attrition by Department Chart
# -----------------------------
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Department",
    hue="Attrition"
)

plt.title("Employee Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/Attrition_by_Department.png"
)

plt.close()


# -----------------------------
# 15. Attrition by Job Role Chart
# -----------------------------
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    y="JobRole",
    hue="Attrition"
)

plt.title("Employee Attrition by Job Role")
plt.xlabel("Employee Count")
plt.ylabel("Job Role")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/Attrition_by_JobRole.png"
)

plt.close()


# -----------------------------
# 16. Salary by Department
# -----------------------------
plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Department",
    y="MonthlyIncome",
    estimator="mean"
)

plt.title("Average Monthly Income by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Income")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/Average_Salary_by_Department.png"
)

plt.close()


# -----------------------------
# 17. Overtime vs Attrition
# -----------------------------
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="OverTime",
    hue="Attrition"
)

plt.title("Overtime vs Employee Attrition")
plt.xlabel("Overtime")
plt.ylabel("Employee Count")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/Overtime_vs_Attrition.png"
)

plt.close()


print("\n----------------------------------")
print("HR ANALYTICS ANALYSIS COMPLETED!")
print("----------------------------------")
print("Analysis files saved in:")
print(output_folder)