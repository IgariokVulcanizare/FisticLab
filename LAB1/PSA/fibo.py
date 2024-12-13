import random

def Fibonacci_numbers(n):
    fib=[1,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[1:]

def Fibonacci_strategy(n):
    fib_bet=Fibonacci_numbers(n)
    buget = 0
    bet = fib_bet[0]
    while (n > 0 and buget < 100 and buget > -100):
        if random.randint(1, 37) <= 18:
            buget += bet
            if (fib_bet.index(bet)-2>=0):
                bet = fib_bet[fib_bet.index(bet)-2]
        else:
            buget -= bet
            bet = fib_bet[fib_bet.index(bet)+1]
        n -= 1
    return buget

n=int(input("enter the number of bets: "))
ex = int(input("enter the number of experiments: "))
bugets=[Fibonacci_strategy(n) for _ in range(ex)]

print("Average profit/loss: ",sum(bugets) / ex)
print("it wont guarantee profit in long term")