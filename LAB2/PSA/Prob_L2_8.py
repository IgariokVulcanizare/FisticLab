import random
n = 10
sitting_brk = []
for i in range(n):
    sitting_brk.append(i)

nr_exp = 10000
permutation = 0
for i in range(nr_exp):
    sitting_ln = sitting_brk[:]
    random.shuffle(sitting_ln)
    win = 0
    for i in range(n):
        if ((sitting_ln[(i+1)%n] != sitting_ln[i] - 1) and (sitting_ln[(i+1)%n] != sitting_ln[i] + 1)
                and (sitting_ln[(i+1)%n] != sitting_ln[(i+2)%n] - 1) and (sitting_ln[(i+1)%n] != sitting_ln[(i+2)%n] + 1)):
            win += 1
        if win == n:
            permutation += 1
print(permutation/nr_exp)
print("For n tends to infinity our probability tends to 1/e^2")#why?

