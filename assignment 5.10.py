import seaborn as sns
import matplotlib.pyplot as plt

# Load the standard "titanic" dataset from seaborn
titanic = sns.load_dataset("titanic")

# Display the first few rows of the dataset
print(titanic.head())

# Create a histogram showing the distribution of passengers' ages
plt.figure(figsize=(10, 6))
sns.histplot(data=titanic, x="age", bins=30, kde=True, color="blue")

# Add title and labels
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Display the histogram
plt.show()
