import random
import matplotlib.pyplot as plt

def DAlembert_strategy(n):
    buget = 0
    bet = 1
    while (n > 0):
        if random.randint(1, 37) <= 18:
            buget += bet
            if (bet != 1):
                bet -= 1
        else:
            buget -= bet
            bet += 1
        n -= 1
    return buget

n=int(input("enter the number of games: "))
ex = int(input("enter the number of experiments you want to make: "))

# Run multiple experiments
budgets = [DAlembert_strategy(n) for _ in range(ex)]

# Calculate statistics
average_budget = sum(budgets) / ex
min_budget = min(budgets)
max_budget = max(budgets)

# Display results
print(f"Average budget: {average_budget}")
print(f"Minimum budget: {min_budget}")
print(f"Maximum budget: {max_budget}")
print("We can see that this strategy fails in long term game")
print("This is because roulette guarantee that the expected amount of money to win is bet*(-0.027)")

# Plot the distribution of budgets
plt.hist(budgets, bins=20, edgecolor="black", color="blue", alpha=0.7)
plt.title("Distribution of Budgets in D'Alembert Strategy")
plt.xlabel("Final Budget")
plt.ylabel("Frequency")
plt.axvline(average_budget, color="red", linestyle="--", label=f"Average: {average_budget:.2f}")
plt.legend()
plt.show()