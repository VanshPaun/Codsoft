import random
import tkinter as tk

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        # Initialize scores
        self.players_points = 0
        self.computers_points = 0

        # Create labels and buttons
        self.label_title = tk.Label(master, text="Rock Paper Scissors", font=("Arial", 20))
        self.label_title.pack(pady=20)

        self.label_player = tk.Label(master, text="Player Score: 0", font=("Arial", 16))
        self.label_player.pack()

        self.label_computer = tk.Label(master, text="Computer Score: 0", font=("Arial", 16))
        self.label_computer.pack()

        self.button_rock = tk.Button(master, text="Rock", command=lambda: self.play("Rock"), width=10, height=2)
        self.button_rock.pack(pady=10)

        self.button_paper = tk.Button(master, text="Paper", command=lambda: self.play("Paper"), width=10, height=2)
        self.button_paper.pack(pady=10)

        self.button_scissor = tk.Button(master, text="Scissors", command=lambda: self.play("Scissors"), width=10, height=2)
        self.button_scissor.pack(pady=10)

        self.label_result = tk.Label(master, text="", font=("Arial", 16))
        self.label_result.pack(pady=10)

    def play(self, user_choice):
        # Computer's choice
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        # Determine winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
            self.players_points += 1
            self.computers_points += 1
        elif (
            (computer_choice == "Paper" and user_choice == "Scissors")
            or (computer_choice == "Rock" and user_choice == "Paper")
            or (computer_choice == "Scissors" and user_choice == "Rock")
        ):
            result = "You Won!"
            self.players_points += 1
        else:
            result = "You Lose!"
            self.computers_points += 1

        # Updates score and display results
        self.label_player.config(text=f"Player Score: {self.players_points}")
        self.label_computer.config(text=f"Computer Score: {self.computers_points}")
        self.label_result.config(text=f"Computer choose {computer_choice}. {result}")

# Create the main window
root = tk.Tk()

# Create the game instance
game = RockPaperScissors(root)

# Start the GUI
root.mainloop()