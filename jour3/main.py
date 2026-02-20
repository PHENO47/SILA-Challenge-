
import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 SciCalc Pro - Jour 3")
        self.root.geometry("400x650")
        
        # État du thème et historique
        self.dark_mode = True
        self.history_list = []
        
        # Configuration des couleurs
        self.colors = {
            "dark":  {"bg": "#1e1e1e", "fg": "#ffffff", "btn": "#333333", "accent": "#fb8c00"},
            "light": {"bg": "#f5f5f5", "fg": "#000000", "btn": "#e0e0e0", "accent": "#ef6c00"}
        }

        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        # --- Zone d'affichage ---
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=0, justify="right")
        self.display.pack(fill="both", padx=10, pady=20)

        # --- Historique Scrollable ---
        self.hist_frame = tk.Frame(self.root)
        self.hist_frame.pack(fill="both", expand=True)
        
        self.scrollbar = tk.Scrollbar(self.hist_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.history_box = tk.Listbox(self.hist_frame, height=4, font=("Arial", 10), 
                                     yscrollcommand=self.scrollbar.set, borderwidth=0)
        self.history_box.pack(fill="both", expand=True, padx=10)
        self.scrollbar.config(command=self.history_box.yview)

        # --- Grille de boutons ---
        self.btns_frame = tk.Frame(self.root)
        self.btns_frame.pack(fill="both", expand=True, padx=5, pady=5)

        buttons = [
            '(', ')', 'C', 'DEL',
            'sin', 'cos', 'tan', '/',
            'log', 'ln', 'sqrt', '*',
            '7', '8', '9', '-',
            '4', '5', '6', '+',
            '1', '2', '3', '^',
            'Theme', '0', '.', '='
        ]

        r, c = 0, 0
        for btn_text in buttons:
            cmd = lambda x=btn_text: self.on_click(x)
            btn = tk.Button(self.btns_frame, text=btn_text, command=cmd, 
                           font=("Arial", 12, "bold"), width=5, height=2, bd=0)
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
            
            c += 1
            if c > 3:
                c = 0
                r += 1

        # Rendre la grille responsive
        for i in range(4): self.btns_frame.columnconfigure(i, weight=1)
        for i in range(7): self.btns_frame.rowconfigure(i, weight=1)

    def on_click(self, char):
        current = self.display.get()
        
        if char == "C":
            self.display.delete(0, tk.END)
        elif char == "DEL":
            self.display.delete(len(current)-1, tk.END)
        elif char == "Theme":
            self.dark_mode = not self.dark_mode
            self.apply_theme()
        elif char == "=":
            self.calculate()
        elif char in ["sin", "cos", "tan", "log", "ln", "sqrt"]:
            self.display.insert(tk.END, f"{char}(")
        elif char == "^":
            self.display.insert(tk.END, "**")
        else:
            self.display.insert(tk.END, char)

    def calculate(self):
        expr = self.display.get()
        try:
            # Remplacement pour la compatibilité math de Python
            safe_expr = expr.replace('sin', 'math.sin').replace('cos', 'math.cos')
            safe_expr = safe_expr.replace('tan', 'math.tan').replace('log', 'math.log10')
            safe_expr = safe_expr.replace('ln', 'math.log').replace('sqrt', 'math.sqrt')
            
            result = eval(safe_expr)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            
            # Ajout à l'historique
            entry = f"{expr} = {result}"
            self.history_box.insert(tk.END, entry)
            self.history_box.see(tk.END)
            
        except ZeroDivisionError:
            messagebox.showerror("Erreur", "Division par zéro impossible")
        except Exception:
            messagebox.showerror("Erreur", "Expression invalide")

    def apply_theme(self):
        theme = self.colors["dark"] if self.dark_mode else self.colors["light"]
        self.root.configure(bg=theme["bg"])
        self.display.configure(bg=theme["bg"], fg=theme["fg"], insertbackground=theme["fg"])
        self.history_box.configure(bg=theme["btn"], fg=theme["fg"])
        
        for btn in self.btns_frame.winfo_children():
            if btn['text'] == "=":
                btn.configure(bg=theme["accent"], fg="white")
            elif not btn['text'].isdigit():
                btn.configure(bg=theme["btn"], fg=theme["accent"])
            else:
                btn.configure(bg=theme["btn"], fg=theme["fg"])

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
