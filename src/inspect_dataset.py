
import pandas as pd

# Load expense dataset
expenses = pd.read_csv("data/raw/expenses.csv")

# Load budget dataset
budgets = pd.read_csv("data/raw/budgets.csv")

print("\n========== EXPENSE DATA ==========")

# Display first 5 records
print("\nFirst 5 records:")
print(expenses.head())

# Display dataset size
print("\nDataset shape:")
print(expenses.shape)

# Display column information2
print("\nColumn information:")
print(expenses.info())

# Check missing values
print("\nMissing values:")
print(expenses.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(expenses.duplicated().sum())

# Basic numerical statistics
print("\nExpense amount statistics:")
print(expenses["amount"].describe())

print("\n========== BUDGET DATA ==========")
print(budgets.head())

print("\nBudget dataset shape:")
print(budgets.shape)


import pandas as pd

print("STARTING DATA INSPECTION...")

expenses = pd.read_csv("data/raw/expenses.csv")
budgets = pd.read_csv("data/raw/budgets.csv")

print("\n--- FIRST FIVE EXPENSES ---")
print(expenses.head())

print("\n--- DATASET SHAPE ---")
print(expenses.shape)

print("\n--- MISSING VALUES ---")
print(expenses.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(expenses.duplicated().sum())

print("\n--- EXPENSE STATISTICS ---")
print(expenses["amount"].describe())

print("\n--- BUDGET DATA ---")
print(budgets.head())

print("\nDATA INSPECTION COMPLETED!")

