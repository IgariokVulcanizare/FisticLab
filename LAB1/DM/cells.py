import random
import matplotlib.pyplot as plt

rule_110 = "01101110" #for "01011010" nice gen gives almost a fractal
rule_110_rev = rule_110[::-1]
rule_map = {f"{i:03b}": int(rule_110_rev[i]) for i in range(8)}


def new_gen(old_gen):
    n = len(old_gen)
    next_gen = []
    for i in range(n):
        # Determine the triplet for the current cell
        if i == 0:
            triplet = f"0{old_gen[i]}{old_gen[i + 1]}"
        elif i == n - 1:
            triplet = f"{old_gen[i - 1]}{old_gen[i]}0"
        else:
            triplet = f"{old_gen[i - 1]}{old_gen[i]}{old_gen[i + 1]}"

        # Determine the new state based on the rule map
        next_gen.append(rule_map[triplet])
    return next_gen


def simulate_generations(initial_gen, generations):
    current_gen = initial_gen
    result = [current_gen]  # Store all generations for visualization
    for _ in range(generations):
        current_gen = new_gen(current_gen)
        result.append(current_gen)
    return result


def visualize(matrix):
    plt.figure(figsize=(10, 10))
    plt.imshow(matrix, cmap="binary", interpolation="nearest")
    plt.axis("off")
    plt.show()


# Generate the initial state randomly
n = int(input("Enter the number of cells: "))
generations = int(input("Enter the number of generations: "))
random_gen = [random.randint(0, 1) for _ in range(n)]

# Simulate 100 generations and visualize
matrix_random = simulate_generations(random_gen, generations)
visualize(matrix_random)

nice_gen = [0 for i in range(n-1)]+[1]
matrix_random = simulate_generations(nice_gen, generations)
visualize(matrix_random)