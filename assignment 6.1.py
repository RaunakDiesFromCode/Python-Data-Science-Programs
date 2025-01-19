import pandas as pd 
emp_dict = { 
'Name': ['Alice', 'Bob', 'Charlie'], 
'Age': [25, 30, 35], 
'Department': ['HR', 'Engineering', 'Sales'] 
} 
df1 = pd.DataFrame(emp_dict) 
print("Dictionary -> Datafrane: Contents of Dataframe1") 
print(df1) 
df2 = pd.read_csv('emp_data.csv') #keep this emp.csv file in the same folder where the code exists. 
print("CSV -> Datafrane: Contents of Dataframe2") 
print(df2) 
df = pd.concat([df1, df2], ignore_index=True) 
print("Dictionary and CSV Concatenated: Contents of Dataframe3") 
print(df) 
selected_df = df[["Name", "Age"]] 
print("Name and Age Columns") 
print(selected_df) 
filtered_df = df[df["Age"] > 25] 
print("Age > 25") 
print(filtered_df) 
df["Salary"] = [50000, 60000, 70000, 45000, 82000, 35000] 
print("Add new column Salary") 
print(df) 
grouped_df = df.groupby("Department")["Age"].mean() 
print("Average Age for each Department") 
print(grouped_df) 
sorted_df = df.sort_values(by="Age", ascending=False) 
print("Sort by the Age column in descending order") 
print(sorted_df) 
mean_salary = df["Salary"].mean() 
median_salary = df["Salary"].median() 
sum_salary = df["Salary"].sum() 
print("Mean, median, and sum of the Salary column") 
print("Mean:", mean_salary) 
print("Median:", median_salary) 
print("Sum:", sum_salary) 