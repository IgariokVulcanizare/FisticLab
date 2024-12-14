import random
import matplotlib.pyplot as plt

def truncate_to_thousands(number):
    return (number // 1000) * 1000

def illegal_riding(exp):
    debts = []
    repeat = 0
    for i in range(exp):
        debt = 0
        if random.random() <= 0.02:
            debt += 6

        if random.random() <= 0.05:
            if repeat == 0:
                debt += 50
            elif repeat == 1:
                debt += 200
            else:
                debt += 300
            repeat += 1
        debts.append(debt)
    return debts

nr_exp = 1000
averages = {}
for k in range(1000, 20000,1000):
    averages.update({k : 0})
for i in range(nr_exp):
    nr_rides = 2*365
    x = truncate_to_thousands(sum(illegal_riding(nr_rides)))
    if (1000 <= x <= 20000):
        averages[x] += 1

legal_student = 2*365*6
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.bar(list(averages.keys()), averages.values(), color='g',width=500)
plt.axvline(x=truncate_to_thousands(legal_student), color='r', linestyle='--', label='Average Legal Cost')
plt.tight_layout()
plt.show()

expectancy = 0
for i in range(1000, 20000,1000):
    expectancy += averages[i]*i

print("If you were Jora(doamne fereste) you would expect to lose: ", expectancy/nr_exp)
print("On the other hand if you are a lawfull student you pay just: ",legal_student)
print("Thus you should pay, otherwise you will eventually lose much more money")
