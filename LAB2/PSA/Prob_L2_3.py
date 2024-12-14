import random

exp = int(input("enter number of experiments: "))
tr=0

for i in range(exp):

    x=random.random()

    if x > 0.5:
        y = random.uniform(0,x)
    else:
        y = random.uniform(x,1)

    first_point = min(x,y)
    second_point = max(x,y)
    side_1 = first_point
    side_2 = 1 - second_point
    side_3 = second_point - first_point

    if ((side_1 +side_2 > side_3) and
            (side_1+side_3 > side_2) and
            (side_2 + side_3 > side_1)):
        tr+=1

print("Probability of getting a triangle is: ",tr/exp)
#need math explanation