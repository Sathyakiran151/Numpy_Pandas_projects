'''🎲 Random Lottery Picker
🧠 Core Idea
You have a list of participants
Randomly pick winners
No repetition → replace=False'''
import numpy as np
arr=np.array(["Alice","Bob","Charlie","sathya","srinath"])
winner =np.random.choice(arr,size=2,replace=False)
print("The Winners are :",winner)


import numpy as np

# Optional: fix randomness for testing (remove in real use)
# np.random.seed(0)

# Step 1: Take input
names = np.array(input("Enter participant names (space-separated): ").split())

k = int(input("Enter number of winners: "))

# Step 2: Validation
if k > len(names):
    print("❌ Error: Number of winners cannot exceed participants")
else:
    # Step 3: Pick winners
    winners = np.random.choice(names, size=k, replace=False)

    # Step 4: Display results nicely
    print("\n🎉 Lottery Results 🎉")
    for i, name in enumerate(winners, start=1):
        if i == 1:
            print(f"🏆 Winner: {name}")
        else:
            print(f"🎖 Runner-up {i-1}: {name}")