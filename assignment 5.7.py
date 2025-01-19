import seaborn as sns
import matplotlib.pyplot as plt

# Load a standard dataset (example: flights dataset from seaborn)
flights = sns.load_dataset("flights")

# Display the first few rows of the dataset
print(flights.head())

# Create a line plot showing the number of passengers over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=flights, x="year", y="passengers",
             hue="month", palette="tab10")

# Add title and labels
plt.title("Number of Airline Passengers Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")

# Display the graph
plt.show()
