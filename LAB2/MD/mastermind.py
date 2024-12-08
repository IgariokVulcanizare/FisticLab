import random

def generate_code(length=4):
    return ''.join(random.choices("0123456789", k=length))

def provide_clues(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_number = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - correct_position
    return correct_position, correct_number

def auto_mode():
    secret = generate_code()
    print("A secret code has been generated. Try to guess it!")

    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        if len(guess) != len(secret):
            print(f"Your guess must be {len(secret)} digits long.")
            continue
        attempts += 1
        correct_position, correct_number = provide_clues(secret, guess)
        if correct_position == len(secret):
            print(f"Congratulations! You guessed the code in {attempts} attempts.")
            break
        else:
            print(f"Clues: {correct_position} digits in the correct position, {correct_number} correct digits in the wrong position.")

def manual_mode():
    secret = input("Enter the secret code for another player to guess: ")
    print("The secret code has been set. Another player will now guess it.")

    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        if len(guess) != len(secret):
            print(f"Your guess must be {len(secret)} digits long.")
            continue
        attempts += 1
        correct_position, correct_number = provide_clues(secret, guess)
        if correct_position == len(secret):
            print(f"Congratulations! You guessed the code in {attempts} attempts.")
            break
        else:
            print(f"Clues: {correct_position} digits in the correct position, {correct_number} correct digits in the wrong position.")

if __name__ == "__main__":
    print("Welcome to Mastermind!")
    mode = input("Choose a mode (auto/manual): ").strip().lower()
    if mode == "auto":
        auto_mode()
    elif mode == "manual":
        manual_mode()
    else:
        print("Invalid mode. Please restart the game and choose 'auto' or 'manual'.")
