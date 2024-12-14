import random
import matplotlib.pyplot as plt

def rolling_dice():
    return random.randint(1,6)

n = int(input("enter number of experiments: "))

frequency = {}

for i in range(3,19):
    frequency.update({i:0})

for i in range(n):
    sum = (rolling_dice()+
           rolling_dice()+
           rolling_dice())

    frequency[sum] += 1

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.bar(list(frequency.keys()), frequency.values(), color='g')
plt.show()

print("we can see that ", frequency[10], " > ", frequency[9])

