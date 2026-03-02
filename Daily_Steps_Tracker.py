import matplotlib.pyplot as plt

# Days of week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Steps walked each day
steps = [4000, 5500, 6000, 5000, 7000, 8000, 6500]

# Plot line graph
plt.plot(days, steps, marker="o")

plt.title("Daily Steps Tracker")
plt.xlabel("Days")
plt.ylabel("Steps Walked")
plt.grid(True)

plt.show()