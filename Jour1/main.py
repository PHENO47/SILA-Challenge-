
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import uuid
from datetime import datetime

# --- LOGIQUE MÉTIER ---
class Compte:
    def __init__(self, titulaire, code, solde=0, numero=None, historique=None):
        self.titulaire = titulaire
        self.code = code
        self.solde = solde
        self.numero = numero or str(uuid.uuid4())[:6].upper()
        self.historique = historique or []

    def tracer(self, op, montant):
        self.historique.append(f"{datetime.now().strftime('%d/%m %H:%M')} | {op}: {montant}€")

# --- INTERFACE GRAPHIQUE STYLISÉE ---
class BanqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏦 MySecureBank v2.0")
        self.root.geometry("450x600")
        self.root.configure(bg="#2c3e50") # Fond bleu nuit moderne
        
        self.comptes = self.charger_donnees()
        
        # Titre
        tk.Label(root, text="MA BANQUE SÉCURISÉE", font=("Helvetica", 18, "bold"), 
                 bg="#2c3e50", fg="#ecf0f1").pack(pady=30)
        
        # Style des boutons
        btn_style = {
            "font": ("Helvetica", 10, "bold"),
            "width": 30,
            "height": 2,
            "bd": 0,
            "cursor": "hand2",
            "activeforeground": "white"
        }

        # Configuration des boutons avec couleurs
        self.creer_bouton("➕ CRÉER UN COMPTE", "#27ae60", self.creer_compte, btn_style)
        self.creer_bouton("📥 DÉPOSER DE L'ARGENT", "#2980b9", self.deposer, btn_style)
        self.creer_bouton("📤 RETIRER DE L'ARGENT", "#e67e22", self.retirer, btn_style)
        self.creer_bouton("💸 VIREMENT BANCAIRE", "#8e44ad", self.virement, btn_style)
        self.creer_bouton("📜 VOIR L'HISTORIQUE", "#95a5a6", self.voir_historique, btn_style)
        
        # Bouton Quitter
        tk.Button(root, text="💾 QUITTER & SAUVEGARDER", command=self.quitter,
                  bg="#c0392b", fg="white", font=("Helvetica", 10, "bold"), 
                  width=30, bd=0).pack(pady=40)

    def creer_bouton(self, texte, couleur, commande, style):
        btn = tk.Button(self.root, text=texte, bg=couleur, fg="white", 
                        command=commande, **style)
        btn.pack(pady=8)

    # --- LOGIQUE DE PERSISTANCE ---
    def charger_donnees(self):
        if os.path.exists("banque_securisee.json"):
            try:
                with open("banque_securisee.json", "r") as f:
                    data = json.load(f)
                    return [Compte(d['titulaire'], d['code'], d['solde'], d['numero'], d['historique']) for d in data]
            except: return []
        return []

    def sauvegarder(self):
        data = [{"titulaire": c.titulaire, "code": c.code, "solde": c.solde, "numero": c.numero, "historique": c.historique} for c in self.comptes]
        with open("banque_securisee.json", "w") as f:
            json.dump(data, f, indent=4)

    def trouver_compte(self, num):
        return next((c for c in self.comptes if c.numero == num.upper()), None)

    # --- ACTIONS ---
    def creer_compte(self):
        nom = simpledialog.askstring("Nouveau", "Nom du titulaire :")
        code = simpledialog.askstring("Sécurité", "Définissez un code secret :", show='*')
        if nom and code:
            nouveau = Compte(nom, code)
            self.comptes.append(nouveau)
            messagebox.showinfo("Succès", f"Compte créé !\nNUMÉRO : {nouveau.numero}\nGardez-le précieusement.")

    def deposer(self):
        num = simpledialog.askstring("Dépôt", "Numéro de compte :")
        if num:
            c = self.trouver_compte(num)
            if c:
                mpt = simpledialog.askfloat("Montant", "Somme à déposer (€) :")
                if mpt and mpt > 0:
                    c.solde += mpt
                    c.tracer("DÉPÔT", mpt)
                    messagebox.showinfo("Confirmé", f"Nouveau solde : {c.solde}€")
            else: messagebox.showerror("Erreur", "Compte introuvable")

    def retirer(self):
        num = simpledialog.askstring("Retrait", "Numéro de compte :")
        if num:
            c = self.trouver_compte(num)
            if c:
                code = simpledialog.askstring("Sécurité", "Code secret :", show='*')
                if code == c.code:
                    mpt = simpledialog.askfloat("Montant", "Somme à retirer (€) :")
                    if mpt and mpt <= c.solde:
                        c.solde -= mpt
                        c.tracer("RETRAIT", mpt)
                        messagebox.showinfo("Succès", f"Argent retiré.\nSolde actuel : {c.solde}€")
                    else: messagebox.showwarning("Alerte", "Solde insuffisant !")
                else: messagebox.showerror("Erreur", "Code incorrect")

    def virement(self):
        src_num = simpledialog.askstring("Virement", "Votre numéro de compte :")
        if src_num:
            src = self.trouver_compte(src_num)
            if src:
                code = simpledialog.askstring("Sécurité", "Votre code secret :", show='*')
                if code == src.code:
                    dest_num = simpledialog.askstring("Virement", "Numéro du bénéficiaire :")
                    dest = self.trouver_compte(dest_num)
                    if dest:
                        mpt = simpledialog.askfloat("Montant", "Somme à envoyer (€) :")
                        if mpt and mpt <= src.solde:
                            src.solde -= mpt
                            dest.solde += mpt
                            src.tracer(f"VIR -> {dest.numero}", mpt)
                            dest.tracer(f"RECU <- {src.numero}", mpt)
                            messagebox.showinfo("Succès", "Virement effectué avec succès !")
                        else: messagebox.showwarning("Alerte", "Solde insuffisant !")
                    else: messagebox.showerror("Erreur", "Bénéficiaire introuvable")
                else: messagebox.showerror("Erreur", "Code incorrect")

    def voir_historique(self):
        num = simpledialog.askstring("Historique", "Numéro de compte :")
        if num:
            c = self.trouver_compte(num)
            if c:
                code = simpledialog.askstring("Sécurité", "Code secret :", show='*')
                if code == c.code:
                    hist_txt = "\n".join(c.historique[-10:]) if c.historique else "Aucun mouvement."
                    messagebox.showinfo(f"Historique de {c.titulaire}", f"10 dernières opérations :\n\n{hist_txt}")
                else: messagebox.showerror("Erreur", "Code incorrect")

    def quitter(self):
        self.sauvegarder()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BanqueApp(root)
    root.mainloop()
