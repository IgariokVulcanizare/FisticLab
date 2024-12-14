import random

def polster(n, threshold=48):
    rep = 0
    for i in range(n):
        if random.randint(1, 100) <= threshold:
            rep += 1
    return (rep / n) * 100

def polstering_people(n, threshold=48):
    right_pred = 0
    aprox_pred = 0

    for i in range(100):
        x = polster(n, threshold)
        if x == threshold:
            right_pred += 1
        if threshold - 0.5 <= x <= threshold + 0.5:
            aprox_pred += 1

    return right_pred, aprox_pred

experimenting_experiments = 100

total_right_pred_1, total_aprox_pred_1 = 0, 0
total_right_pred_2, total_aprox_pred_2 = 0, 0

for i in range(experimenting_experiments):
    right_pred_1, aprox_pred_1 = polstering_people(1000, threshold=48)
    total_right_pred_1 += right_pred_1
    total_aprox_pred_1 += aprox_pred_1

    right_pred_2, aprox_pred_2 = polstering_people(1000, threshold=49)
    total_right_pred_2 += right_pred_2
    total_aprox_pred_2 += aprox_pred_2

print("For threshold 48:")
print(f"Average correct predictions: {total_right_pred_1 / experimenting_experiments}")#out of 100
print(f"Average within 1% margin: {total_aprox_pred_1 / experimenting_experiments}")

print("\nFor threshold 49:")
print(f"Average correct predictions: {total_right_pred_2 / experimenting_experiments}")
print(f"Average within 1% margin: {total_aprox_pred_2 / experimenting_experiments}")

experimenting_experiments = 100

total_right_pred_1, total_aprox_pred_1 = 0, 0
total_right_pred_2, total_aprox_pred_2 = 0, 0

for i in range(experimenting_experiments):
    right_pred_1, aprox_pred_1 = polstering_people(3000, threshold=48)
    total_right_pred_1 += right_pred_1
    total_aprox_pred_1 += aprox_pred_1

    right_pred_2, aprox_pred_2 = polstering_people(3000, threshold=49)
    total_right_pred_2 += right_pred_2
    total_aprox_pred_2 += aprox_pred_2

print("\nFor threshold 48:")
print(f"Average correct predictions: {total_right_pred_1 / experimenting_experiments}")
print(f"Average within 1% margin: {total_aprox_pred_1 / experimenting_experiments}")

print("\nFor threshold 49:")
print(f"Average correct predictions: {total_right_pred_2 / experimenting_experiments}")
print(f"Average within 1% margin: {total_aprox_pred_2 / experimenting_experiments}")
