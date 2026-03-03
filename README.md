🏥 Healthcare Risk & Patient Analytics Dashboard


📌 Project Overview

This project analyzes 30,000 patient healthcare records to identify clinical risk drivers, behavioral health patterns, and hospitalization trends.

The objective is to transform raw clinical and lifestyle data into actionable healthcare intelligence using data analytics and interactive visualization.

🎯 Project Objectives

Identify high-risk medical conditions

Analyze lifestyle factors impacting health outcomes

Examine hospitalization and recovery patterns

Segment patients into risk categories

Provide data-driven healthcare recommendations

📊 Dataset Details

Records: 30,000 patients

Features: 20 clinical & behavioral variables

Data Types: Numeric, categorical, engineered metrics

Missing Data: ~15% handled via statistical imputation

Key Variables:

Age

Medical Condition

Glucose

BMI

Cholesterol

Smoking

Alcohol

Stress Level

Sleep Hours

Length of Stay

🧹 Data Engineering Process
1️⃣ Data Cleaning

Standardized medical indicators

Handled missing values using imputation

Removed noise features

2️⃣ Feature Engineering

Created Risk Score segmentation

Built Age Group categories

Engineered behavioral health metrics

3️⃣ Database Integration

Exported cleaned dataset to PostgreSQL

Performed advanced SQL queries

Used aggregation and segmentation logic

🛠 Technology Stack

Python

Pandas & NumPy

SQL (PostgreSQL)

Plotly

Dash

Jupyter Notebook

📈 Dashboard Features

✔ Interactive slicers (Medical Condition, Smoking, Alcohol, Risk Level)
✔ KPI Cards (Total Patients, Avg Risk, Avg Stay, Avg Cholesterol)
✔ 10 Advanced Visualizations
✔ Dark professional UI theme
✔ Section-based structured layout

🔍 Key Insights

Metabolic conditions (Diabetes & Obesity) show highest average risk scores

Smoking strongly correlates with elevated cholesterol levels

Higher BMI associated with longer hospital stays

Stress negatively impacts sleep duration

Risk severity increases progressively with age

Combined lifestyle + chronic conditions amplify hospitalization duration

🏥 Business & Healthcare Impact

This analysis supports:

Preventive care targeting high-risk patients

Lifestyle intervention programs

Resource optimization in hospitals

Age-based screening prioritization

Behavioral health support initiatives

🚀 Strategic Recommendations

Implement preventive care programs for metabolic-risk patients

Promote smoking and obesity reduction initiatives

Align hospital capacity with high-risk segments

Strengthen behavioral health monitoring systems


▶ How to Run Dashboard
1️⃣ Install Dependencies
pip install pandas plotly dash
2️⃣ Run Dashboard
python dashboard.py
3️⃣ Open in Browser
http://127.0.0.1:8050
📌 Conclusion

This project demonstrates a complete healthcare analytics workflow:

Raw Data → Cleaning → SQL Analysis → Risk Modeling → Interactive Dashboard → Strategic Recommendations

It highlights the integration of clinical data analytics with business intelligence principles to support informed healthcare decision-making.

🏆 Author

Rohit Sharma
Data Analytics Enthusiast
Python | SQL | Dashboard Development
