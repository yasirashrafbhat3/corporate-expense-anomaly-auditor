
import pandas as pd
import numpy as np
from pathlib import Path

# Make the dataset reproducible
np.random.seed(42)

# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Company information
departments = ["Finance", "HR", "IT", "Marketing", "Sales"]

categories = [
    "Travel",
    "Food",
    "Office Supplies",
    "Software",
    "Accommodation",
    "Training"
]

payment_methods = [
    "Credit Card",
    "Debit Card",
    "Bank Transfer",
    "Cash"
]

vendors = [
    "ABC Travels",
    "Global Hotels",
    "Tech Solutions",
    "Office World",
    "Food Express",
    "Cloud Services",
    "City Transport",
    "Learning Hub"
]

# Generate 1,000 normal expense records
records = []

for i in range(1000):

    department = np.random.choice(departments)
    category = np.random.choice(categories)

    # Typical expense amounts based on category
    amount_ranges = {
        "Travel": (1500, 7000),
        "Food": (200, 1500),
        "Office Supplies": (300, 2500),
        "Software": (1000, 8000),
        "Accommodation": (2000, 9000),
        "Training": (1000, 6000)
    }

    low, high = amount_ranges[category]

    amount = round(np.random.uniform(low, high), 2)

    expense_date = pd.Timestamp("2025-01-01") + pd.Timedelta(
        days=int(np.random.randint(0, 365))
    )

    records.append({
        "expense_id": f"EXP{i + 1:04d}",
        "employee_id": f"EMP{np.random.randint(101, 151)}",
        "department": department,
        "category": category,
        "amount": amount,
        "expense_date": expense_date,
        "payment_method": np.random.choice(payment_methods),
        "vendor": np.random.choice(vendors)
    })

expenses = pd.DataFrame(records)

# Plant 12 unusual high-value expenses
anomaly_labels = []

for i in range(12):

    index = 1000 - 12 + i

    expenses.loc[index, "amount"] = np.random.uniform(
        30000, 60000
    )

    expense_id = expenses.loc[index, "expense_id"]

    anomaly_labels.append({
        "expense_id": expense_id,
        "test_label": "planted_high_amount"
    })

# Add 5 duplicate transaction candidates
duplicates = expenses.sample(
    n=5,
    random_state=42
).copy()

for i in range(len(duplicates)):
    original_id = duplicates.iloc[i]["expense_id"]

    duplicates.iloc[i, duplicates.columns.get_loc("expense_id")] = (
        f"EXP_DUP{i + 1:03d}"
    )

    anomaly_labels.append({
        "expense_id": f"EXP_DUP{i + 1:03d}",
        "test_label": "planted_duplicate"
    })

# Combine original records and duplicate candidates
expenses = pd.concat(
    [expenses, duplicates],
    ignore_index=True
)

# Create monthly department budgets
budget_records = []

monthly_budgets = {
    "Finance": 120000,
    "HR": 80000,
    "IT": 180000,
    "Marketing": 150000,
    "Sales": 140000
}

for month in range(1, 13):

    for department in departments:

        budget_records.append({
            "department": department,
            "year": 2025,
            "month": month,
            "budget": monthly_budgets[department]
        })

budgets = pd.DataFrame(budget_records)

# Save datasets
expenses.to_csv(
    RAW_DIR / "expenses.csv",
    index=False
)

budgets.to_csv(
    RAW_DIR / "budgets.csv",
    index=False
)

pd.DataFrame(anomaly_labels).to_csv(
    PROCESSED_DIR / "synthetic_test_labels.csv",
    index=False
)

print("DATASET GENERATION COMPLETED!")
print("--------------------------------")
print("Expense records:", len(expenses))
print("Department budgets:", len(budgets))
print("Planted test cases:", len(anomaly_labels))
print("\nDepartment distribution:")
print(expenses["department"].value_counts())
print("\nCategory distribution:")
print(expenses["category"].value_counts())
print("\nSaved files:")
print("data/raw/expenses.csv")
print("data/raw/budgets.csv")
print("data/processed/synthetic_test_labels.csv")