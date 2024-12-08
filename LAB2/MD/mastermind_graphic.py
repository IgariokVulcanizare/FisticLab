import random
import tkinter as tk
from tkinter import messagebox

def generate_code(length=4):
    return ''.join(random.choices("0123456789", k=length))

def provide_clues(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_number = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - correct_position
    return correct_position, correct_number

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind")

        self.secret_code = generate_code()
        self.attempts = 0

        self.label = tk.Label(root, text="Enter your guess (4 digits):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.clues_label = tk.Label(root, text="")
        self.clues_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        if len(guess) != len(self.secret_code):
            messagebox.showerror("Error", f"Your guess must be {len(self.secret_code)} digits long.")
            return

        self.attempts += 1
        correct_position, correct_number = provide_clues(self.secret_code, guess)

        if correct_position == len(self.secret_code):
            messagebox.showinfo("Congratulations!", f"You guessed the code in {self.attempts} attempts.")
            self.clues_label.config(text="")
        else:
            self.clues_label.config(text=f"Clues: {correct_position} digits in the correct position, {correct_number} correct digits in the wrong position.")

    def reset_game(self):
        self.secret_code = generate_code()
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.clues_label.config(text="")
        messagebox.showinfo("Game Reset", "A new game has started. Try to guess the code!")

if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()
