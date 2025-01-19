import seaborn as sns
import matplotlib.pyplot as plt

# Load the standard "iris" dataset from seaborn
iris = sns.load_dataset("iris")

# Display the first few rows of the dataset
print(iris.head())

# Create a scatter plot showing sepal length vs. sepal width
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width",
                hue="species", palette="deep", s=100)

# Add title and labels
plt.title("Sepal Length vs. Sepal Width (Iris Dataset)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

# Display the scatter plot
plt.show()
