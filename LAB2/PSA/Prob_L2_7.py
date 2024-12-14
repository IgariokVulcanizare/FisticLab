import random
import matplotlib.pyplot as plt

def number_of_heads():
    nr_heads = 0
    for i in range(100):
        if random.random() < 0.5:
            nr_heads += 1
    return nr_heads

nr_exp = 1000
frequency = {}
for i in range(35,66):
    frequency.update({i:0})

for k in range(nr_exp):
    x = number_of_heads()
    if (34 < x < 66):
        frequency[x] += 1
print(frequency)

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.bar(list(frequency.keys()), frequency.values(), color='g')
plt.show()
print("For bigger number of experiments it looks like Normal Distribution")
print("Explanation: for large n Binomial D -> Normal D because of Stirling")#is that so?