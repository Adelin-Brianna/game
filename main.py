import tkinter as tk
from PIL import ImageTk, Image
import itertools
import random

class RockPaperScissorsGame:
    def __init__(self, win):
        self.win = win
        self.win.title("Rock Paper Scissors Game")
        self.win.config(bg="darkgreen")

        # Configure grid
        for i in range(5):
            self.win.grid_columnconfigure(i, weight=1)
        for i in range(8):
            self.win.grid_rowconfigure(i, weight=1)

        # Title Label
        tk.Label(self.win, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"), padx=20, pady=10, bg="darkgreen", fg="white").grid(row=0, column=0, columnspan=5, sticky="nsew")

        # Load and resize images
        self.rock_image = ImageTk.PhotoImage(Image.open("rock.jpg").resize((100, 100), Image.LANCZOS))
        self.paper_image = ImageTk.PhotoImage(Image.open("paper.jpg").resize((100, 100), Image.LANCZOS))
        self.scissors_image = ImageTk.PhotoImage(Image.open("scissors.jpg").resize((100, 100), Image.LANCZOS))

        self.images = itertools.cycle([self.rock_image, self.paper_image, self.scissors_image])

        # Rock buttons
        user_rock_button = tk.Button(self.win, image=self.rock_image, bg="darkgreen", borderwidth=0, command=lambda: self.user_choice("rock"))
        user_rock_button.grid(row=2, column=0, columnspan=1, pady=10)

        system_rock_button = tk.Button(self.win, image=self.rock_image, bg="darkgreen", borderwidth=0)
        system_rock_button.grid(row=4, column=4, columnspan=1, pady=10)

        # Paper buttons
        user_paper_button = tk.Button(self.win, image=self.paper_image, bg="darkgreen", borderwidth=0, command=lambda: self.user_choice("paper"))
        user_paper_button.grid(row=3, column=0, columnspan=1, pady=10)

        system_paper_button = tk.Button(self.win, image=self.paper_image, bg="darkgreen", borderwidth=0)
        system_paper_button.grid(row=2, column=4, columnspan=1, pady=10)

        # Scissors buttons
        user_scissors_button = tk.Button(self.win, image=self.scissors_image, bg="darkgreen", borderwidth=0, command=lambda: self.user_choice("scissors"))
        user_scissors_button.grid(row=4, column=0, columnspan=1, pady=10)

        system_scissors_button = tk.Button(self.win, image=self.scissors_image, bg="darkgreen", borderwidth=0)
        system_scissors_button.grid(row=3, column=4, columnspan=1, pady=10)

        # Toggling image
        self.middle_label_user = tk.Label(self.win, bg="darkgreen")
        self.middle_label_user.grid(row=3, column=1, columnspan=1, pady=10)  # User choice

        self.middle_label_system = tk.Label(self.win, bg="darkgreen")
        self.middle_label_system.grid(row=3, column=3, columnspan=1, pady=10)  # System choice

        # choice 
        self.system_choice_label = tk.Label(self.win, text="", bg="darkgreen")
        self.system_choice_label.grid(row=5, column=0, columnspan=5, pady=10)

        # Result 
        self.result_label = tk.Label(self.win, text="", bg="darkgreen", fg="white", font=("Helvetica", 16))
        self.result_label.grid(row=6, column=0, columnspan=5, pady=20)

        # Replay and Quit buttons
        replay_button = tk.Button(self.win, text="Replay", command=self.replay, padx=20, pady=10, bg="yellow", font=("Helvetica", 14, "bold"))
        replay_button.grid(row=7, column=1, columnspan=1, pady=10)

        quit_button = tk.Button(self.win, text="Quit", command=self.quit, padx=20, pady=10, bg="red", font=("Helvetica", 14, "bold"))
        quit_button.grid(row=7, column=3, columnspan=1, pady=10)

        # Animation control
        self.animation_running = True
        self.update_image()

    def update_image(self):
        if self.animation_running:
            self.middle_label_user.config(image=next(self.images))
            self.middle_label_system.config(image=next(self.images))
            self.win.after(100, self.update_image)

    def stop_animation(self):
        self.animation_running = False

    def start_animation(self):
        self.animation_running = True
        self.update_image()

    def user_choice(self, choice):
        self.stop_animation()
        system_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(choice, system_choice)
        self.display_result(choice, system_choice, result)

    def determine_winner(self, user_choice, system_choice):
        if user_choice == system_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and system_choice == "scissors") or \
             (user_choice == "paper" and system_choice == "rock") or \
             (user_choice == "scissors" and system_choice == "paper"):
            return "You win!"
        else:
            return "System wins!"

    def display_result(self, user_choice, system_choice, result):
        choices = {
            "rock": self.rock_image,
            "paper": self.paper_image,
            "scissors": self.scissors_image
        }
        self.middle_label_user.config(image=choices[user_choice])  
        self.middle_label_system.config(image=choices[system_choice])  
        self.result_label.config(text=f"{result}")

    #Replay the game
    def replay(self):
        self.start_animation()
        self.system_choice_label.config(text="")
        self.result_label.config(text="")

    #Close window
    def quit(self):
        self.win.quit()  

# Create the main window
win = tk.Tk()
game = RockPaperScissorsGame(win)
win.mainloop()
