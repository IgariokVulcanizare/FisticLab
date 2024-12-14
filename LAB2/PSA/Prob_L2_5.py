import random

def birth_until_boy():
    nr_babies = 0
    while True:
        if random.random() < 0.5:
            nr_babies+=1
            break
        nr_babies+=1
    return nr_babies


nr_exp = int(input("nr of experiments: "))
sum = 0
for i in range(nr_exp):
    sum += birth_until_boy()
print("On average we have: ", sum/nr_exp)
print("Thus the will to have a boy doesn't change the expectancy")

def birth_until_boy_and_girl():
    nr_boys = 0
    nr_girls = 0
    while (nr_boys == 0 or nr_girls == 0):
        if random.random() < 0.5:
            nr_boys+=1
        else:
            nr_girls+=1
    return nr_boys+nr_girls

sum = 0
for i in range(nr_exp):
    sum += birth_until_boy_and_girl()
print("\nOn average we have: ", sum/nr_exp, " until the first boy and girl")
print("This result is logic: you have either boy or girls\n"
      "then you just have to give the birth to only the remained gender\n"
      "and the expectancy of that from previous point is 2\n")

nr_of_families = 100_000#what a nice feature!
birthday_tactic_1 = 0
birthday_tactic_2 = 0
for i in range(nr_of_families):
    birthday_tactic_1 += birth_until_boy()
    birthday_tactic_2 += birth_until_boy_and_girl()
print("using second tactic and 100 000 families we expect to have : "
      ,abs(birthday_tactic_1 - birthday_tactic_2) / nr_of_families, " more children")