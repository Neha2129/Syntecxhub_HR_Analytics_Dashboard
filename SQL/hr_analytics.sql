CREATE DATABASE IF NOT EXISTS hr_analytics;
USE hr_analytics;

CREATE TABLE IF NOT EXISTS employees (
    EmployeeNumber INT PRIMARY KEY,
    Age INT,
    Attrition VARCHAR(10),
    BusinessTravel VARCHAR(50),
    DailyRate INT,
    Department VARCHAR(100),
    DistanceFromHome INT,
    Education INT,
    EducationField VARCHAR(100),
    EmployeeCount INT,
    EnvironmentSatisfaction INT,
    Gender VARCHAR(20),
    HourlyRate INT,
    JobInvolvement INT,
    JobLevel INT,
    JobRole VARCHAR(100),
    JobSatisfaction INT,
    MaritalStatus VARCHAR(30),
    MonthlyIncome INT,
    MonthlyRate INT,
    NumCompaniesWorked INT,
    Over18 VARCHAR(5),
    OverTime VARCHAR(10),
    PercentSalaryHike INT,
    PerformanceRating INT,
    RelationshipSatisfaction INT,
    StandardHours INT,
    StockOptionLevel INT,
    TotalWorkingYears INT,
    TrainingTimesLastYear INT,
    WorkLifeBalance INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT
);employees

USE hr_analytics;

SELECT COUNT(*) AS Total_Employees
FROM employees;

USE hr_analytics;

SELECT COUNT(*) AS Total_Employees
FROM `WA_Fn-UseC_-HR-Employee-Attrition`;

SELECT *
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
LIMIT 5;

USE hr_analytics;

SELECT COUNT(*) AS Total_Employees
FROM `WA_Fn-UseC_-HR-Employee-Attrition`;

USE hr_analytics;

-- 1. Total Employees
SELECT COUNT(*) AS Total_Employees
FROM `WA_Fn-UseC_-HR-Employee-Attrition`;

-- 2. Attrition Count
SELECT COUNT(*) AS Attrition_Count
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
WHERE Attrition = 'Yes';

-- 3. Retention Count
SELECT COUNT(*) AS Retention_Count
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
WHERE Attrition = 'No';

-- 4. Attrition Rate
SELECT
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`;

-- 5. Retention Rate
SELECT
    ROUND(
        SUM(CASE WHEN Attrition = 'No' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Retention_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`;

SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY Department
ORDER BY Attrition_Rate DESC;

SELECT
    JobRole,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY JobRole
ORDER BY Attrition_Rate DESC;

SELECT
    Department,
    ROUND(AVG(MonthlyIncome), 2) AS Average_Salary,
    MIN(MonthlyIncome) AS Minimum_Salary,
    MAX(MonthlyIncome) AS Maximum_Salary
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY Department
ORDER BY Average_Salary DESC;

SELECT
    Department,
    ROUND(AVG(TotalWorkingYears), 2) AS Average_Total_Working_Years,
    ROUND(AVG(YearsAtCompany), 2) AS Average_Years_At_Company
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY Department
ORDER BY Average_Total_Working_Years DESC;

SELECT
    OverTime,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY OverTime
ORDER BY Attrition_Rate DESC;

SELECT
    JobSatisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

SELECT
    Gender,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY Gender
ORDER BY Attrition_Rate DESC;

SELECT
    PerformanceRating,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM `WA_Fn-UseC_-HR-Employee-Attrition`
GROUP BY PerformanceRating
ORDER BY PerformanceRating;