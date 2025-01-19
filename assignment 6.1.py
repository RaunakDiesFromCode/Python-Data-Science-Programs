import pandas as pd

# Create a dictionary and convert it to a DataFrame
emp_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Department': ['HR', 'Engineering', 'Sales']
}
df1 = pd.DataFrame(emp_dict)
print("Dictionary -> DataFrame: Contents of DataFrame1")
print(df1)

# Read data from a CSV file into a DataFrame
# Keep this emp.csv file in the same folder where the code exists.
df2 = pd.read_csv('emp_data.csv')
print("CSV -> DataFrame: Contents of DataFrame2")
print(df2)

# Concatenate the two DataFrames
df = pd.concat([df1, df2], ignore_index=True)
print("Dictionary and CSV Concatenated: Contents of DataFrame3")
print(df)

# Select specific columns
selected_df = df[["Name", "Age"]]
print("Name and Age Columns")
print(selected_df)

# Filter rows based on a condition
filtered_df = df[df["Age"] > 25]
print("Age > 25")
print(filtered_df)

# Add a new column to the DataFrame
df["Salary"] = [50000, 60000, 70000, 45000, 82000, 35000]
print("Add new column Salary")
print(df)

# Group by a column and calculate the mean of another column
grouped_df = df.groupby("Department")["Age"].mean()
print("Average Age for each Department")
print(grouped_df)

# Sort the DataFrame by a column in descending order
sorted_df = df.sort_values(by="Age", ascending=False)
print("Sort by the Age column in descending order")
print(sorted_df)

# Calculate mean, median, and sum of a column
mean_salary = df["Salary"].mean()
median_salary = df["Salary"].median()
sum_salary = df["Salary"].sum()
print("Mean, median, and sum of the Salary column")
print("Mean:", mean_salary)
print("Median:", median_salary)
print("Sum:", sum_salary)
