import seaborn as sns
import matplotlib.pyplot as plt

# Load the standard "tips" dataset from seaborn
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
print(tips.head())

# Create a bar plot showing the total bill for each day
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x="day", y="total_bill", estimator=sum, palette="muted")

# Add title and labels
plt.title("Total Bill per Day (Tips Dataset)")
plt.xlabel("Day")
plt.ylabel("Total Bill (Sum)")

# Display the bar plot
plt.show()
