import random
import matplotlib.pyplot as plt

def generating_sequence():
    x = random.random()
    y = 0
    nr = 0
    while y < x:
        y =random.random()
        nr += 1
    return nr


nr_avrg_experiment = 1000
nr_el_aver = 100
averages = {}
for i in range(nr_el_aver):
    averages.update({i:0})
for i in range(nr_avrg_experiment):
    nr_exp = 1000
    payout = []
    for i in range(nr_exp):
        payout.append(generating_sequence())
    average = int(sum(payout)/nr_exp)
    if average < nr_el_aver:
        averages[average] += 1
print(averages)
print(sum(averages.values())/nr_el_aver)

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.bar(list(averages.keys()), averages.values(), color='g')
plt.show()

print("Giving the bigger and bigger number of experiments we can see that payout tends to infinity")#math
