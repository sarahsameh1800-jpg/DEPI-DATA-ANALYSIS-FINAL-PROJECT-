import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

performance_rating = pd.read_csv('HR/PerformanceRating.csv')
employee = pd.read_csv('HR/Employee.csv')
educational_level = pd.read_csv('HR/EducationLevel.csv')
rating_level = pd.read_csv('HR/RatingLevel.csv')
satisfied_level = pd.read_csv('HR/SatisfiedLevel.csv')

#basic EDA on each table individually

def eda(df, name):
    print(f"--- EDA for {name} ---")
    print("Head:")
    print(df.head())
    print("\nInfo:")
    print(df.info())
    print("\nDescription:")
    print(df.describe(include='all'))
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\n Duplicated Rows:")
    print(df.duplicated().sum())
    print("\n" + "-"*40 + "\n")

# eda(performance_rating, "Performance Rating")
# eda(employee, "Employee")
# eda(educational_level, "Educational Level")
# eda(rating_level, "Rating Level")
# eda(satisfied_level, "Satisfied Level")

# no missing values or duplicates found in any table
# checking for inconsistent data types
def check_data_types(df, name):
    print(f"--- Data Types for {name} ---")
    print(df.dtypes)
    print("\n" + "-"*40 + "\n")

# check_data_types(performance_rating, "Performance Rating")
# check_data_types(employee, "Employee")
# check_data_types(educational_level, "Educational Level")
# check_data_types(rating_level, "Rating Level")
# check_data_types(satisfied_level, "Satisfied Level")

#dates are in object format, converting to datetime

employee['HireDate'] = pd.to_datetime(employee['HireDate'], errors='coerce')
performance_rating['ReviewDate'] = pd.to_datetime(performance_rating['ReviewDate'], errors='coerce')

#salary should be numeric
employee['Salary'] = pd.to_numeric(employee['Salary'], errors='coerce')

#box plot to check for outliers in Salary
employee.boxplot(column='Salary')
plt.title('Box plot of Salary')
plt.ylabel('Salary')
plt.show()

#salarys are beyond the IQR but in a consistent range, so no removal of outliers

#corr plot to check relationships
corr = employee.select_dtypes(include=['number']).corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix for Employee Numerical Features')
plt.show()
#no new insights from correlation matrix

#merging tables
merged_df = performance_rating.merge(employee, on='EmployeeID', how='left')
merged_df = merged_df.merge(educational_level, left_on='Education', right_on='EducationLevelID', how='left')

# merge rating_level twice with distinct column suffixes
rating_self = rating_level.copy().add_suffix('_Self')
rating_manager = rating_level.copy().add_suffix('_Manager')
merged_df = merged_df.merge(rating_self, left_on='SelfRating', right_on='RatingID_Self', how='left')
merged_df = merged_df.merge(rating_manager, left_on='ManagerRating', right_on='RatingID_Manager', how='left')

# merge satisfied_level for multiple satisfaction columns with distinct suffixes
s_env = satisfied_level.copy().add_suffix('_Env')
s_job = satisfied_level.copy().add_suffix('_Job')
s_rel = satisfied_level.copy().add_suffix('_Rel')
s_wlb = satisfied_level.copy().add_suffix('_WLB')
merged_df = merged_df.merge(s_env, left_on='EnvironmentSatisfaction', right_on='SatisfactionID_Env', how='left')
merged_df = merged_df.merge(s_job, left_on='JobSatisfaction', right_on='SatisfactionID_Job', how='left')
merged_df = merged_df.merge(s_rel, left_on='RelationshipSatisfaction', right_on='SatisfactionID_Rel', how='left')
merged_df = merged_df.merge(s_wlb, left_on='WorkLifeBalance', right_on='SatisfactionID_WLB', how='left')

print(merged_df.head())

merged_df.to_csv('HR/Merged_HR_Data.csv', index=False)

