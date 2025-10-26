# Bank Customer Churn Analysis

This project explores customer churn in a bank dataset using **Exploratory Data Analysis (EDA)** techniques.  
The objective is to identify patterns and insights that may explain why some customers leave the bank while others stay.

## 📁 Dataset Details
- File: https://drive.google.com/file/d/1ayaK-Tk5iT7NFVPDCxlfTRAVZc-sm4QK/view?usp=drive_link
- Source: Kaggle
- **Attributes:**
 - CreditScore
 - Geography
 - Gender
 - Age
 - Tenure
 - Balance
 - NumOfProducts
 - HasCrCard
 - IsActiveMember
 - EstimatedSalary
 - Exited (Target Variable - Churn: 1 = Yes, 0 = No)

## 📊 Tools & Libraries Used
- Python 🐍
- Pandas
- Matplotlib
- Seaborn

## 🔍 EDA Steps Performed
- Loaded and cleaned the dataset
- Handled missing values and checked data types
- Visualized churn distribution
- Analyzed impact of demographic features (Age, Gender, Geography)
- Analyzed customer behavior (Tenure, Product usage, Activity)
- Explored financial indicators (Credit Score, Balance, Salary)
- Calculated correlation matrix

## 🎯 Key Insights
- Customers aged 40+ and inactive users had higher churn rates.
- German customers showed significantly more churn.
- Tenure, number of products, and account balance influenced churn risk.
- Salary and credit score had minimal impact.

## 📈 Visualizations Included
- Pie & Donut Charts → Attrition distribution by gender, department, and job role
- Bar Charts → Attrition by age group, education, business travel, overtime, and marital status
- Stacked Bar Charts → Attrition across job roles segmented by salary slab and years at company
- Histograms → Employee age distribution, monthly income spread
- Boxplots → Monthly income vs. attrition, years at company vs. attrition
- Heatmap / Correlation Matrix → Relationship between key numerical features (e.g., job satisfaction, environment satisfaction, income, tenure)

## ✅ Final Result
This EDA-based analysis helped uncover high-risk customer segments, enabling banks to strategize better retention campaigns.

## 🙋‍♂️ Author
#### Fathima Shahanas


