import pandas as pd

# Load employee data from CSV file
df = pd.read_csv("employees.csv")

# Display all employee records
print("\n===== Employee Data =====")
print(df.to_string(index=False))

# Calculate average salary
average_salary = df["Salary"].mean()

print("\n===== Average Salary =====")
print("Average Salary:", round(average_salary, 2))

# Count employees in each department
print("\n===== Department-wise Employee Count =====")
department_count = df["Department"].value_counts()
print(department_count)

# Filter employees earning more than 50000
salary_threshold = 50000

high_salary = df[df["Salary"] > salary_threshold]

print("\n===== Employees Earning More Than 50000 =====")
print(high_salary.to_string(index=False))

# Export filtered data to a new CSV file
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered employee data saved to high_salary_employees.csv")