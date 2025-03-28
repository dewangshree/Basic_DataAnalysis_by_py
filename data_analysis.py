import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("sample_data.csv")

# Basic Info
print("Dataset Overview:")
print(df.info())

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Visualization: Salary Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Salary"], bins=20, kde=True, color="blue")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Visualization: Age vs. Experience
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Age"], y=df["Experience (Years)"], hue=df["Department"])
plt.title("Age vs. Experience")
plt.xlabel("Age")
plt.ylabel("Experience (Years)")
plt.legend(title="Department")
plt.show()
