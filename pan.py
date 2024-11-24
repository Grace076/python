import pandas as pd

# Step 1: Load the dataset
# Replace 'your_dataset.csv' with the path to your dataset file
file_path = 'expense data.csv'.csv'
try:
    data = pd.read_csv(file_path)
    print("Dataset successfully loaded!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()

# Step 2: Display the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Step 3: Explore the structure of the dataset
print("\nDataset information:")
print(data.info())

print("\nSummary statistics:")
print(data.describe())

print("\nMissing values in each column:")
print(data.isnull().sum())

# Step 4: Clean the dataset
# Option 1: Fill missing values with a default value (e.g., mean for numeric columns, 'Unknown' for strings)
data_cleaned = data.fillna({
    col: data[col].mean() if data[col].dtype in ['float64', 'int64'] else "Unknown"
    for col in data.columns
})

# Option 2: Drop rows with any missing values
# data_cleaned = data.dropna()

print("\nMissing values after cleaning:")
print(data_cleaned.isnull().sum())

# Display the cleaned dataset's first few rows
print("\nFirst 5 rows of the cleaned dataset:")
print(data_cleaned.head())
#2
import pandas as pd

# Load the dataset
# Replace 'your_dataset.csv' with your actual dataset file
file_path = 'expense data.csv'

try:
    data = pd.read_csv(file_path)
    print("Dataset successfully loaded!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()

# Display the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Step 1: Compute basic statistics
print("\nBasic statistics of numerical columns:")
print(data.describe())

# Step 2: Group by a categorical column and compute mean for each group
# Replace 'categorical_column' with the actual column name, and 'numerical_column' with the numerical column you want to analyze
categorical_column = 'categorical_column'
numerical_column = 'numerical_column'

if categorical_column in data.columns and numerical_column in data.columns:
    print(f"\nMean of '{numerical_column}' grouped by '{categorical_column}':")
    group_means = data.groupby(categorical_column)[numerical_column].mean()
    print(group_means)
else:
    print(f"Error: Columns '{categorical_column}' and/or '{numerical_column}' not found in the dataset.")

# Step 3: Analyze patterns or interesting findings
# Example: Print the group with the highest mean
if categorical_column in data.columns and numerical_column in data.columns:
    max_mean_group = group_means.idxmax()
    max_mean_value = group_means.max()
    print(f"\nInteresting finding: The group '{max_mean_group}' has the highest mean value of {numerical_column}: {max_mean_value:.2f}")
