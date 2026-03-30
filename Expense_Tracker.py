import numpy as np

# Input expenses
expenses = np.array(list(map(float, input("Enter daily expenses: ").split())))

# Calculations
total = np.sum(expenses)
average = np.mean(expenses)
highest = np.max(expenses)
lowest = np.min(expenses)

# High spending days (> average)
high_days = expenses[expenses > average]

# Output
print("\n📊 Expense Report")
print("Expenses:", expenses)
print("Total Expense:", total)
print("Average Expense:", average)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)

print("\n💸 High Spending Days (above average):", high_days)