# DEPI DATA ANALYSIS FINAL PROJECT
This is our final project where we take a deep dive in HR files to analyse for trends and performance metrics and gather key insights from the given data

# Team Members:
1- Fady Wagdy Naeem
2- Omar Reda Kassem
3- Omar Reda Kamel
4- Sarah Sameh Abdelazeem 
5- Mahmoud Ahmed Elsayed

# Files

The Given HR Folder from DEPI containing the following files:
-EducationLevel.csv
-Employee.csv
-PerformanceRating.csv
-RatingLevel.csv
-SatisfiedLevel.csv

## Description for each file

   ### Employee.csv
        EmployeeID                → Unique alphanumeric identifier for each employee.
        FirstName                 → Employee’s first name.
        LastName                  → Employee’s last name.
        Gender                    → Employee’s gender (Male, Female, etc.).
        Age                       → Employee’s age in years.
        BusinessTravel             → Frequency of business travel (No Travel, Some Travel, Frequent Travel).
        Department                → Department where the employee works (Sales, HR, R&D, etc.).
        DistanceFromHome (KM)     → Distance between home and office in kilometers.
        State                     → U.S. state abbreviation where the employee is located.
        Ethnicity                 → Ethnic background of the employee (White, Asian, Black, Hispanic, etc.).
        Education                 → Numeric code for education level (links to EducationLevel.csv).
        EducationField            → Field of study related to education (Life Sciences, Marketing, etc.).
        JobRole                   → Job title or position (Sales Executive, Research Scientist, etc.).
        MaritalStatus             → Marital status (Single, Married, Divorced).
        Salary                    → Annual salary in USD.
        StockOptionLevel          → Level of stock options awarded (0–3).
        OverTime                  → Indicates if the employee works overtime (Yes/No).
        HireDate                  → Date employee was hired (YYYY-MM-DD).
        Attrition                 → Whether the employee has left the company (Yes/No).
        YearsAtCompany            → Total years worked at the company.
        YearsInMostRecentRole     → Years in the most recent role.
        YearsSinceLastPromotion   → Years since the last promotion.
        YearsWithCurrManager      → Years with the current manager.

   ### PerformanceRating.csv
        PerformanceID                    → Unique ID for each performance review record.
        EmployeeID                       → Links to Employee.csv.
        ReviewDate                       → Date of review (MM/DD/YYYY).
        EnvironmentSatisfaction          → Satisfaction with work environment (1–5, links to SatisfiedLevel.csv).
        JobSatisfaction                  → Satisfaction with the job (1–5).
        RelationshipSatisfaction         → Satisfaction with workplace relationships (1–5).
        TrainingOpportunitiesWithinYear  → Number of training opportunities provided.
        TrainingOpportunitiesTaken       → Number of training sessions attended.
        WorkLifeBalance                  → Perception of work-life balance (1–5).
        SelfRating                       → Self-evaluation score (1–5).
        ManagerRating                    → Manager’s rating score (1–5).

   ### EducationLevel.csv
        EducationLevelID   → Numeric identifier for education level.
        EducationLevel     → Label for the education level.

        Example values:
            1 → No Formal Qualifications
            2 → High School
            3 → Bachelors
            4 → Masters
            5 → Doctorate

   ### SatisfiedLevel.csv
        SatisfactionID     → Numeric identifier for satisfaction level.
        SatisfactionLevel  → Text description of satisfaction level.

        Example values:
            1 → Very Dissatisfied
            2 → Dissatisfied
            3 → Neutral
            4 → Satisfied
            5 → Very Satisfied

   ### RatingLevel.csv
        RatingID     → Numeric identifier for performance rating (1–5).
        RatingLevel  → Text description of the rating label.

        Example values:
            1 → Unacceptable
            2 → Needs Improvement
            3 → Meets Expectations
            4 → Exceeds Expectations
            5 → Above and Beyond

##  UML Diagram
![UML Diagram](images/diagram.jpg)

--------

# EDA
## Overview
clean.py prepares the raw HR datasets for analysis by validating, normalizing, and exporting cleaned CSV files. Running the script produces cleaned datasets in the cleaned_data folder.
Purpose
- Normalize column names and datatypes. - Handle missing or inconsistent values (drop or impute based on rules). - Map numeric codes to human-readable labels using lookup files. - Produce reproducible, analysis-ready CSV files.
Expected inputs
The script expects the raw CSV files (as provided in the project) to be available in the input folder (project root or configured input path):
- Employee.csv - PerformanceRating.csv - EducationLevel.csv - SatisfiedLevel.csv - RatingLevel.csv
Outputs
- Cleaned CSV files saved to the cleaned_data folder (one cleaned file per input file). - Optional log messages printed to console or saved to a log file (depending on implementation).
Dependencies
- Python 3.8+ - pandas (for CSV I/O and transformations) - numpy (optional, for numeric operations) List additional packages in requirements.txt if used.
Main steps performed (high level)
- Load raw CSVs into DataFrame(s). - Standardize column names (trim, lowercase, replace spaces). - Convert date columns to datetime (e.g., HireDate, ReviewDate). - Convert numeric columns to appropriate numeric dtypes (ages, years, salary). - Map code fields using lookup files (e.g., Education → EducationLevel). - Normalize categorical values (e.g., OverTime: Yes/No). - Handle missing or invalid data (drop or impute, with consistent rules). - Save cleaned outputs to cleaned_data.
## Usage
install dependencies:
```
pip install -r requirements.txt
```
run the cleaning script:
```
python clean.py
```
The cleaned CSV files will be saved in the cleaned_data folder.

# Analysis
## Goals
### Overview Analysis

-----------------------------------
1. Total number of employees.
2. Trends in hired and Reviewed employees over the years.
3. Employee distribution by department and job role.
4. Count of employees at HQ vs. other branches.
5. City distribution of employees.
-----------------------------------
### Demographic Analysis

-----------------------------------
1. Genders distribution.
2. Age distribution.
3. Education levels distribution.
4. Education and Performance correlation
-----------------------------------
### Income Analysis

-----------------------------------
1. Patterns in salary distribution across education levels and genders.
2. Age and Salary correlation across departments.
-----------------------------------

## Charts 
The analysis was conducted and presented using Tableau.
The Tableau workbook file is included in the repository as "HR Analysis.twbx".

### Key Findings
1. Total Hired 6,709
2. Average salary $111,062
3. Average Years at Company 5.7

4. Decline in Hired employees from 2012 to 2022
![Hiring trendline](images/hire_over_years.png)

5. on the contrary Reviews increased during the same time
![Review trendline](images/review_over_years.png)

6. Department Distribution
![Department Distribution](images/department_distribution.png)
- Sub distribution by Job Role
![Tech Roles Distribution](images/tech_department_distribution.png)
- Sales Roles Distribution
![Sales Roles Distribution](images/sales_department_distribution.png)
- HR Roles Distribution
![HR Roles Distribution](images/HR_department_distribution.png)
- Overall Job Role Distribution
![Overall Job Role Distribution](images/jobrole_department_distribution.png)
7. State Distribution

      ![State Distribution](images/states_distribution.png)
8. Gender Distribution

      ![Gender Distribution](images/Gender_distribution.png)
9. Age Education Distribution

      ![Age Education Distribution](images/Age_education_orr.png)
10.  Age Salary Distribution

      ![Age Salary Distribution](images/age_salary_corr.png)
11.  Education Level Performance Distribution

      ![Education Level Performance Distribution](images/Education_performance_corr.png)
12.  Gender, Education Level Salary Distribution

      ![Gender, Education Level Salary Distribution](images/gender_salary_education_corr.png)



## Dashboard
A dashboard was created in Tableau to visualize the key metrics and trends identified in the analysis. The dashboard includes interactive charts and graphs that allow users to explore the data in more detail.
The Tableau workbook file is included in the repository as "HR Analysis.twbx".
### Dashboard Screenshots
1. Overview Dashboard (dark mode)
![Overview Dashboard](images/dark_mode_summary.png)
2. Overview Dashboard (light mode)
![Overview Dashboard](images/light_mode_summary.png)
3. Employee Detailed List (dark mode)
![Employee Detailed List](images/employee_list_dark_mode.png)
4. Employee Detailed List (light mode)
![Employee Detailed List](images/employee_list_light_mode.png)

## How to Use the Dashboard
1. Open the Tableau workbook file "HR Analysis.twbx" using Tableau Desktop or Tableau Reader.
2. Navigate through the different sheets and dashboards to explore the data.
3. Use filters and interactive elements to drill down into specific metrics or segments of the data.
4. Analyze trends and patterns to gain insights into the HR data.
5. Export visualizations or data as needed for reporting or presentations.
6. Save any changes made to the workbook for future reference.
7. Share the workbook with stakeholders to facilitate data-driven decision-making in HR management.
8. Refer to the key findings section for insights derived from the analysis.

# Conclusion
This analysis provided insights into the HR data, revealing trends in hiring, employee demographics, and salary
distribution. Key findings include a decline in hiring over the years, gender disparities in salary, and correlations between education levels and performance ratings. These insights can inform HR strategies and decision-making.






