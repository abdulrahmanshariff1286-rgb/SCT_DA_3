### HR Employee Attrition Analytics Pipeline & Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI" />
  <img src="https://img.shields.io/badge/Data_Analytics-FF6F00?style=for-the-badge&logo=google-analytics&logoColor=white" alt="Data Analytics" />
</p>

<p align="center">
  <strong>An end-to-end data extraction, transformation, and visualization project identifying the core drivers of workforce turnover.</strong>
</p>

---

## 📊 Dashboard Previews

<p align="center">
  <img width="1295" height="729" alt="Dashboard_for_Task_3" src="https://github.com/user-attachments/assets/55024ddf-7156-4b00-b6f9-3980b60ac207" />

</p>


---

## 📑 Table of Contents
- [Executive Summary](#-executive-summary)
- [The Business Problem](#-the-business-problem)
- [Dataset Overview](#-dataset-overview)
- [Methodology & Architecture](#-methodology--architecture)
- [Key Business Insights](#-key-business-insights)
- [Installation & Reproduction](#-installation--reproduction)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

## 🚀 Executive Summary
This project delivers a comprehensive analytical solution to monitor, analyze, and understand employee attrition. By engineering a Python-based data processing script, raw HR records are transformed into aggregated, business-ready metrics. These metrics are then consumed by a Microsoft Power BI dashboard, providing HR leadership with an interactive tool to drill down into departmental vulnerabilities and role-specific turnover rates.

## 🏢 The Business Problem
Unplanned employee turnover (attrition) is a massive financial drain on modern enterprises, resulting in steep recruitment costs, loss of institutional knowledge, and decreased team morale. 

**The objective of this analysis is to:**
1. Establish a quantitative baseline for the current organizational attrition rate.
2. Isolate high-risk departments and job roles experiencing disproportionate turnover.
3. Provide an intuitive, visual reporting tool for non-technical stakeholders to make data-backed retention decisions.

---

## 📂 Dataset Overview
The analysis utilizes two robust HR datasets (`HR_Attrition.csv` and an extended feature set `WA_Fn-UseC_-HR-Employee-Attrition.csv`). 

**Key Dimensions Analyzed:**
* **Demographics:** Age, Gender, Marital Status, Education Field.
* **Job Characteristics:** Department, Job Role, Job Level, Business Travel frequency.
* **Compensation & Tenure:** Monthly Income, Percent Salary Hike, Years at Company, Years in Current Role.
* **Satisfaction Metrics:** Environment Satisfaction, Job Involvement, Work-Life Balance.
* **Target Variable:** `Attrition` (Boolean: Yes/No indicating if the employee left the company).

---

## 🧠 Methodology & Architecture

### 1. Data Ingestion & Transformation (Python)
* **Library Utilization:** Leveraged `pandas` for high-performance data manipulation.
* **Metric Calculation:** Engineered logic to calculate the exact percentage of the workforce that has left the company, isolating the `Yes` values in the target column.
* **Grouping & Aggregation:** Grouped raw records by `Department` and `JobRole`, applying lambda functions to calculate localized attrition rates.
* **Data Export:** Automated the generation of clean `.csv` files (`attrition_by_department.csv`, `attrition_by_role.csv`) to serve as structured inputs for downstream BI tools.

### 2. Exploratory Data Analysis (EDA)
* Utilized `matplotlib` and `seaborn` to programmatically generate static visualizations (e.g., `attrition_by_department.png`) for quick programmatic health checks of the data distribution before building the full dashboard.

### 3. Business Intelligence (Power BI)
* Imported the raw and processed datasets into Power BI.
* Developed interactive KPI cards, bar charts, and demographic breakdowns to allow users to slice the data dynamically based on their specific inquiry.

---

## 💡 Key Business Insights
Based on the execution of the analytical pipeline:
* **Baseline Volatility:** The Python script successfully quantified the total organizational attrition rate, providing a necessary benchmark for future HR initiatives.
* **Departmental Risk:** The aggregated data explicitly highlights operational sectors with the highest flight risk, allowing for targeted managerial intervention.
* **Role-Specific Turnover:** By sorting the grouped data in descending order, the analysis immediately surfaces the most vulnerable job roles, indicating potential systemic issues with compensation, career progression, or burnout in those specific positions.

---

---

## 💻 Installation & Reproduction

### Prerequisites
* Python 3.8+
* Microsoft Power BI Desktop

### Step 1: Clone the Repository
```bash
git clone [https://github.com/yourusername/hr-attrition-analytics.git](https://github.com/yourusername/hr-attrition-analytics.git)
cd hr-attrition-analytics
```

### Step 2: Install Python Dependencies
```bash
pip install pandas matplotlib seaborn
```

### Step 3: Execute the Data Pipeline
Run the exploration script. *Note: Ensure your working directory matches the script's file paths, or update the file paths in the script to relative paths (e.g., `./Data/HR_Attrition.csv`).*
```bash
python Scripts/HR_Data_Exploration_for_Task_3.py
```
This will print the baseline attrition rate to your console and generate the output files in your directory.

### Step 4: Launch the Dashboard
Open `Dashboard/Task_3_dashboard.pbix` in Power BI Desktop to interact with the visualizations.

---

## 🔭 Future Scope
To further elevate this project, future iterations could include:
* **Predictive Modeling:** Implementing Machine Learning algorithms (such as Random Forest or Logistic Regression) using `scikit-learn` to predict the probability of a *current* employee leaving, shifting the analysis from descriptive to predictive.
* **Automated Data Pipelines:** Orchestrating the script execution using workflow automation tools to update the dashboard data dynamically.

---

## 👨‍💻 Author
**Abdul Rahman** Information Science Engineering | Data Science & Full Stack Development Enthusiast based in Bangalore.

* [LinkedIn Profile](www.linkedin.com/in/abdul-rahman-56117b291)
* [GitHub Profile](https://github.com/abdulrahmanshariff1286-rgb)
* **Email:** abdulrahmanshariff1286@gmail.com
```
