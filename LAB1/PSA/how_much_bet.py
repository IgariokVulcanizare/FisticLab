import numpy as np
import matplotlib.pyplot as plt

def simulate_game(num_games):
    """
    Simulates a given number of games and returns a list of payouts.
    """
    payouts = []
    for _ in range(num_games):
        tosses = 1
        while np.random.random() > 0.5:  # Continue tossing until the first head
            tosses += 1
        payouts.append(2 ** tosses)  # Payout is 2^tosses
    return payouts

def simulate_game_batch(batch_size):
    """
    Simulates a batch of games and returns the sum of payouts and the batch size.
    """
    total_payout = 0
    for _ in range(batch_size):
        tosses = 1
        while np.random.random() > 0.5:  # Continue tossing until the first head
            tosses += 1
        total_payout += 2 ** tosses  # Payout is 2^tosses
    return total_payout, batch_size

def compute_average_n_power_n(n):
    """
    Computes the average payout for a simulation of n^n games using batch processing.
    """
    total_games = n ** n
    batch_size = 10 ** 6
    num_batches = total_games // batch_size
    remaining_games = total_games % batch_size

    total_payout = 0
    total_count = 0

    # Simulate in batches
    for batch in range(num_batches):
        batch_payout, batch_count = simulate_game_batch(batch_size)
        total_payout += batch_payout
        total_count += batch_count
        print(f"Processed batch {batch + 1}/{num_batches}...")  # Progress update

    # Simulate remaining games
    if remaining_games > 0:
        batch_payout, batch_count = simulate_game_batch(remaining_games)
        total_payout += batch_payout
        total_count += batch_count

    # Compute average
    average_payout = total_payout / total_count
    return average_payout

# Main Program
num_games = int(input("Enter the number of games: "))

# Simulate individual games
payouts = simulate_game(num_games)
average_payout = sum(payouts) / num_games
max_payout = max(payouts)

# Simulate batch games for n^n games
average_payout_regular = compute_average_n_power_n(num_games)

# Display results
print(f"Number of Games: {num_games}")
print(f"Average Payout: {average_payout:.2f}")
print(f"Number of Games Simulated: {num_games ** num_games}")
print(f"Average Payout For Regular People: {average_payout_regular:.2f}") # cat ar trebui sa betuiesti ca sa nu iesi pe minus (max)
print(f"Maximum Payout: {max_payout}")

# Highlight extreme payouts
extreme_threshold = 1000  # Define "extremely high" payouts
extreme_count = sum(payout > extreme_threshold for payout in payouts)
print(f"Number of Payouts > ${extreme_threshold}: {extreme_count} ({(extreme_count / num_games) * 100:.2f}%)")

# Plot cumulative distribution
sorted_payouts = np.sort(payouts)
cumulative_prob = np.arange(1, len(sorted_payouts) + 1) / len(sorted_payouts)
plt.figure(figsize=(10, 6))
plt.plot(sorted_payouts, cumulative_prob, label='Cumulative Probability', color='blue')
plt.axhline(0.99, color='red', linestyle='--', label='99% of payouts')
plt.title('Cumulative Distribution of Payouts')
plt.xlabel('Payout ($)')
plt.ylabel('Cumulative Probability')
plt.xscale('log')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
