import json
import os
import uuid
from datetime import datetime

# --- EXCEPTIONS PERSONNALISÉES ---
class BanqueErreur(Exception): pass
class SoldeInsuffisantError(BanqueErreur): pass
class PlafondDepasseError(BanqueErreur): pass
class AuthentificationError(BanqueErreur): pass

# --- CLASSES LOGIQUE MÉTIER ---
class Compte:
    def __init__(self, titulaire, code_secret, solde=0, numero=None, historique=None):
        self.titulaire = titulaire
        self.__code_secret = code_secret # Attribut privé
        self.solde = solde
        self.numero = numero or str(uuid.uuid4())[:6].upper()
        self.historique = historique or []

    def verifier_code(self, code):
        if self.__code_secret != code:
            raise AuthentificationError("Code secret incorrect !")
        return True

    def tracer(self, type_op, montant):
        self.historique.append({
            "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "op": type_op,
            "montant": montant,
            "solde_final": self.solde
        })

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            self.tracer("DEPOT", montant)
            return True
        return False

    def retirer(self, montant, code):
        self.verifier_code(code)
        if montant > self.solde:
            raise SoldeInsuffisantError(f"Solde insuffisant ({self.solde}€)")
        self.solde -= montant
        self.tracer("RETRAIT", montant)

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "titulaire": self.titulaire,
            "code": self.__code_secret,
            "solde": self.solde,
            "numero": self.numero,
            "historique": self.historique
        }

class ComptePro(Compte):
    def retirer(self, montant, code):
        self.verifier_code(code)
        if self.solde - montant < -1000:
            raise PlafondDepasseError("Découvert autorisé de 1000€ dépassé !")
        self.solde -= montant
        self.tracer("RETRAIT_PRO", montant)

# --- PERSISTANCE DES DONNÉES ---
DB_FILE = "banque_securisee.json"

def charger_donnees():
    if not os.path.exists(DB_FILE): return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            comptes = []
            for d in data:
                cls = ComptePro if d['type'] == 'ComptePro' else Compte
                comptes.append(cls(d['titulaire'], d['code'], d['solde'], d['numero'], d['historique']))
            return comptes
    except: return []

def sauvegarder_donnees(comptes):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in comptes], f, indent=4)

# --- INTERFACE UTILISATEUR (CLI) ---
def menu_principal():
    comptes = charger_donnees()
    
    while True:
        print("\n" + "="*40)
        print(" 🏦 SYSTEME BANCAIRE POO - SECURE ")
        print("="*40)
        print("1. 🆕 Créer un compte")
        print("2. 📥 Déposer de l'argent")
        print("3. 📤 Retirer de l'argent (Code requis)")
        print("4. 💸 Faire un virement (Code requis)")
        print("5. 📜 Voir l'historique (Code requis)")
        print("6. 💾 Quitter et Sauvegarder")
        
        choix = input("\n👉 Votre choix : ")

        try:
            if choix == "1":
                nom = input("Nom du titulaire : ")
                code = input("Définissez un code secret : ")
                type_c = input("Type (1: Standard, 2: Pro/Découvert) : ")
                nouveau = ComptePro(nom, code) if type_c == "2" else Compte(nom, code)
                comptes.append(nouveau)
                print(f"✅ Compte créé ! Numéro unique : {nouveau.numero}")

            elif choix == "2":
                num = input("Numéro de compte : ")
                c = next((x for x in comptes if x.numero == num), None)
                if c:
                    mpt = float(input("Montant à déposer : "))
                    c.deposer(mpt)
                    print(f"✅ Succès ! Nouveau solde : {c.solde}€")
                else: print("❌ Compte introuvable.")

            elif choix in ["3", "4", "5"]:
                num = input("Votre numéro de compte : ")
                c = next((x for x in comptes if x.numero == num), None)
                if not c:
                    print("❌ Compte introuvable.")
                    continue
                
                if choix == "3":
                    mpt = float(input("Montant à retirer : "))
                    code = input("Code secret : ")
                    c.retirer(mpt, code)
                    print(f"✅ Retrait effectué. Solde : {c.solde}€")
                
                elif choix == "4":
                    dest_num = input("Numéro du destinataire : ")
                    dest = next((x for x in comptes if x.numero == dest_num), None)
                    if dest:
                        mpt = float(input("Montant du virement : "))
                        code = input("Votre code secret : ")
                        c.retirer(mpt, code)
                        dest.deposer(mpt)
                        print(f"✅ Virement de {mpt}€ envoyé à {dest.titulaire}.")
                    else: print("❌ Destinataire introuvable.")
                
                elif choix == "5":
                    code = input("Code secret : ")
                    c.verifier_code(code)
                    print(f"\n📜 HISTORIQUE - {c.titulaire} ({c.numero})")
                    for h in c.historique:
                        print(f"[{h['date']}] {h['op']} : {h['montant']}€ (Solde : {h['solde_final']}€)")

            elif choix == "6":
                sauvegarder_donnees(comptes)
                print("👋 Fermeture sécurisée. À bientôt !")
                break

        except BanqueErreur as e:
            print(f"⚠️ ERREUR : {e}")
        except ValueError:
            print("⚠️ Erreur : Saisie numérique invalide.")

if __name__ == "__main__":
    menu_principal()
