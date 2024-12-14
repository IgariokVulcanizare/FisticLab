import random

def flip_a_coin_on_board():
    win = 0
    x = random.uniform(0,8)
    y = random.uniform(0,8)

    frac_x = x-int(x)
    frac_y = y-int(y)

    if (0.25 <= frac_x <= 0.75) and (0.25 <= frac_y <= 0.75):
        return 1
    else:
        return 0

nr_exp = int(input("How many times would you like to flip the coin? "))
win = 0
for i in range(nr_exp):
    win += flip_a_coin_on_board()
print("The probability that you win is: ",win/nr_exp)
print("The expected value the is = ", 1*(win/nr_exp) + (-0.25)*(1-win/nr_exp))
print("Thus the game is not fair, player has an advantage")#daca inteleg corect conditia
#daca conditia am inteleso gresit game is fair ca expected value e 0.