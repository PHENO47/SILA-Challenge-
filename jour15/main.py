import tkinter as tk
from tkinter import ttk, messagebox
from word_loader import WordLoader


class HangmanGame:

    def __init__(self, root):

        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("520x650")

        self.loader = WordLoader()

        self.score = 0
        self.word = self.loader.get_word()

        self.guessed = []
        self.errors = 0
        self.max_errors = 6

        self.choose_theme()
        self.setup_ui()

    def choose_theme(self):

        answer = messagebox.askquestion(
            "Thème",
            "Activer le mode sombre ?"
        )

        if answer == "yes":

            self.bg = "#1e1e1e"
            self.fg = "white"
            self.btn = "#2e2e2e"

        else:

            self.bg = "#f5f5f5"
            self.fg = "black"
            self.btn = "#e0e0e0"

        self.root.configure(bg=self.bg)

    def setup_ui(self):

        title = tk.Label(
            self.root,
            text="HANGMAN GAME",
            font=("Helvetica",28,"bold"),
            bg=self.bg,
            fg=self.fg
        )
        title.pack(pady=15)

        self.score_label = tk.Label(
            self.root,
            text=f"Score : {self.score}",
            font=("Helvetica",16),
            bg=self.bg,
            fg=self.fg
        )
        self.score_label.pack()

        self.canvas = tk.Canvas(
            self.root,
            width=200,
            height=250,
            bg=self.bg,
            highlightthickness=0
        )
        self.canvas.pack(pady=10)

        self.word_label = tk.Label(
            self.root,
            font=("Helvetica",28,"bold"),
            bg=self.bg,
            fg=self.fg
        )
        self.word_label.pack(pady=20)

        self.update_word()

        keyboard_frame = tk.Frame(self.root, bg=self.bg)
        keyboard_frame.pack()

        letters = "abcdefghijklmnopqrstuvwxyz"

        for i, letter in enumerate(letters):

            btn = tk.Button(
                keyboard_frame,
                text=letter.upper(),
                width=4,
                height=2,
                font=("Helvetica",10,"bold"),
                bg=self.btn,
                fg=self.fg,
                activebackground="#4CAF50",
                command=lambda l=letter: self.guess(l)
            )

            btn.grid(row=i // 7, column=i % 7, padx=4, pady=4)

        restart_btn = tk.Button(
            self.root,
            text="Nouvelle Partie",
            font=("Helvetica",12,"bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.restart
        )

        restart_btn.pack(pady=20)

    def update_word(self):

        display = ""

        for letter in self.word:

            if letter in self.guessed:
                display += letter + " "
            else:
                display += "_ "

        self.word_label.config(text=display)

    def guess(self, letter):

        if letter in self.guessed:
            return

        self.guessed.append(letter)

        if letter not in self.word:

            self.errors += 1
            self.draw_hangman()

        self.update_word()

        if all(l in self.guessed for l in self.word):

            self.score += 10
            self.score_label.config(text=f"Score : {self.score}")

            messagebox.showinfo("Victoire","Bravo ! +10 points")

            self.restart()

        if self.errors >= self.max_errors:

            messagebox.showinfo("Perdu",f"Le mot était : {self.word}")

            self.restart()

    def draw_hangman(self):

        if self.errors == 1:
            self.canvas.create_line(20,230,180,230, fill=self.fg)

        elif self.errors == 2:
            self.canvas.create_line(50,230,50,20, fill=self.fg)

        elif self.errors == 3:
            self.canvas.create_line(50,20,140,20, fill=self.fg)

        elif self.errors == 4:
            self.canvas.create_line(140,20,140,50, fill=self.fg)

        elif self.errors == 5:
            self.canvas.create_oval(120,50,160,90, outline=self.fg)

        elif self.errors == 6:
            self.canvas.create_line(140,90,140,150, fill=self.fg)

    def restart(self):

        self.canvas.delete("all")

        self.word = self.loader.get_word()

        self.guessed = []
        self.errors = 0

        self.update_word()


root = tk.Tk()
app = HangmanGame(root)
root.mainloop()