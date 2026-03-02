import matplotlib.pyplot as plt

# Expense categories
categories = ["Food", "Travel", "Rent"]

# Amount spent
amount = [3000, 1500, 8000]

# Bar chart
plt.bar(categories, amount,color="green")

plt.title("Monthly Expenses")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")

plt.show()