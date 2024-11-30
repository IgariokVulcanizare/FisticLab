#adjacent bullets
import random
n = int(input("Enter the number of experiments: "))
print("Experiment 1: 6 barrel and 2 adjacent bullets")
win_no_spin=0
win_spin=0
for i in range(n):
    barrel=[0,0,0,0,0,0]
    r1 = random.randint(0, 5)
    barrel[r1]=1
    barrel[(r1+1)%6]=1

    while True:
        shoot=random.randint(0, 5)
        if barrel[shoot]==0:
            break
    if barrel[(shoot+1)%6] == 0:
        win_no_spin+=1
    if barrel[random.randint(0,5)] == 0:
        win_spin+=1
print("The probability that you survive if don't spin is ",win_no_spin/n)
print("The probability that you survive if spin is ",win_spin/n)

if win_no_spin > win_spin:
    print("You shouldn't spin\n")
else:
    print("You should spin\n")

#non_adjacent bullets
print("Experiment 2: 6 barrel and 2 non_adjacent bullets")
win_no_spin=0
win_spin=0
for i in range(n):
    barrel=[0,0,0,0,0,0]
    r1 = random.randint(0, 5)
    barrel[r1]=1
    r2 = random.randint(0, 5)
    while r1 == r2 or r1 == r2-1 or r1 == (r2+1)%6:
        r2 = random.randint(0, 5)
    barrel[r2]=1

    while True:
        shoot=random.randint(0, 5)
        if barrel[shoot]==0:
            break
    if barrel[(shoot+1)%6] == 0:
        win_no_spin+=1
    if barrel[random.randint(0,5)] == 0:
        win_spin+=1
print("The probability that you survive if don't spin is ",win_no_spin/n)
print("The probability that you survive if spin is ",win_spin/n)

if win_no_spin > win_spin:
    print("You shouldn't spin\n")
else:
    print("You should spin\n")

print("Experiment 3: 5 barrel and 2 adjacent bullets")
win_no_spin=0
win_spin=0
for i in range(n):
    barrel=[0,0,0,0,0]
    r1 = random.randint(0, 4)
    barrel[r1]=1
    barrel[(r1+1)%5]=1

    while True:
        shoot=random.randint(0, 4)
        if barrel[shoot]==0:
            break
    if barrel[(shoot+1)%5] == 0:
        win_no_spin+=1
    if barrel[random.randint(0,4)] == 0:
        win_spin+=1
print("The probability that you survive if don't spin is ",win_no_spin/n)
print("The probability that you survive if spin is ",win_spin/n)

if win_no_spin > win_spin:
    print("You shouldn't spin\n")
else:
    print("You should spin\n")

print("Experiment 4: 5 barrel and 2 non_adjacent bullets")
win_no_spin=0
win_spin=0
for i in range(n):
    barrel=[0,0,0,0,0]
    r1 = random.randint(0, 4)
    barrel[r1]=1
    r2 = random.randint(0, 4)
    while r1 == r2 or r1 == r2-1 or r1 == (r2+1)%5:
        r2 = random.randint(0, 4)
    barrel[r2]=1

    while True:
        shoot=random.randint(0, 4)
        if barrel[shoot]==0:
            break
    if barrel[(shoot+1)%5] == 0:
        win_no_spin+=1
    if barrel[random.randint(0,4)] == 0:
        win_spin+=1
print("The probability that you survive if don't spin is ",win_no_spin/n)
print("The probability that you survive if spin is ",win_spin/n)

if win_no_spin > win_spin:
    print("You shouldn't spin\n")
else:
    print("You should spin\n")