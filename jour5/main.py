import random
from collections import Counter
import time

# --- CLASSES DE BASE (Carte, Deck) ---
class Carte:
    SYMBOLES = {'Coeur': '♥', 'Carreau': '♦', 'Trèfle': '♣', 'Pique': '♠'}
    VALEURS = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    def __init__(self, valeur, enseigne):
        self.valeur = valeur
        self.enseigne = enseigne

    def __repr__(self):
        return f"[{self.VALEURS[self.valeur]}{self.SYMBOLES[self.enseigne]}]"

class Deck:
    def __init__(self):
        self.cartes = [Carte(v, e) for v in range(2, 15) for e in Carte.SYMBOLES]
        random.shuffle(self.cartes)

    def tirer(self, n=1):
        return [self.cartes.pop() for _ in range(n)]

# --- LOGIQUE D'ÉVALUATION ---
class Evaluateur:
    @staticmethod
    def evaluer(main_complete):
        valeurs = sorted([c.valeur for c in main_complete], reverse=True)
        enseignes = [c.enseigne for c in main_complete]
        compte_v = Counter(valeurs)
        frequences = sorted(compte_v.values(), reverse=True)
        
        # Détection Couleur et Quinte
        couleur = any(enseignes.count(e) >= 5 for e in Carte.SYMBOLES)
        valeurs_uniques = sorted(list(set(valeurs)))
        quinte = any(valeurs_uniques[i+4] - valeurs_uniques[i] == 4 for i in range(len(valeurs_uniques)-4))
        
        if couleur and quinte: return 8, "Quinte Flush"
        if 4 in frequences: return 7, "Carré"
        if 3 in frequences and 2 in frequences: return 6, "Full"
        if couleur: return 5, "Couleur"
        if quinte: return 4, "Quinte"
        if 3 in frequences: return 3, "Brelan"
        if frequences.count(2) >= 2: return 2, "Double Paire"
        if 2 in frequences: return 1, "Paire"
        return 0, "Hauteur"

# --- SYSTÈME DE JEU INTERACTIF ---
class Joueur:
    def __init__(self, nom, est_bot=True):
        self.nom = nom
        self.main = []
        self.est_bot = est_bot
        self.en_jeu = True

    def simuler_proba(self, board, deck_restant):
        victoires = 0
        sims = 300
        for _ in range(sims):
            test_deck = random.sample(deck_restant, len(deck_restant))
            b_complet = board + test_deck[:5-len(board)]
            adv = test_deck[5:7]
            if Evaluateur.evaluer(self.main + b_complet)[0] >= Evaluateur.evaluer(adv + b_complet)[0]:
                victoires += 1
        return (victoires / sims) * 100

def duel_poker():
    print("      ♣️ ♦️ POKER HOLD'EM INTERACTIF v2 ♠️ ♥️")
    print("-" * 45)
    
    deck = Deck()
    joueur = Joueur("Toi", est_bot=False)
    bot = Joueur("Bot-IA")
    board = []

    # Distribution initiale
    joueur.main = deck.tirer(2)
    bot.main = deck.tirer(2)

    etapes = [("FLOP", 3), ("TURN", 1), ("RIVER", 1)]

    for nom_etape, nb_cartes in etapes:
        print(f"\n--- {nom_etape} ---")
        board += deck.tirer(nb_cartes)
        print(f"Board : {board}")
        print(f"Ta main : {joueur.main}")
        
        # Aide à la décision (Monte-Carlo)
        proba = joueur.simuler_proba(board, deck.cartes)
        print(f"💡 Chance de gain estimée : {proba:.1f}%")

        # Interaction
        choix = input(f"[{joueur.nom}] (C)ontinuer ou (S)e coucher ? ").upper()
        if choix == 'S':
            print("❌ Tu t'es couché. Le Bot gagne le pot !")
            return

        # Decision du Bot (IA basique)
        bot_proba = bot.simuler_proba(board, deck.cartes)
        if bot_proba < 15: # Le bot se couche si ses chances sont trop faibles
            print(f"🤖 {bot.nom} trouve sa main trop faible et se couche ! Tu gagnes !")
            return
        else:
            print(f"🤖 {bot.nom} décide de suivre...")
        
        time.sleep(1)

    # Showdown
    print("\n" + "="*20 + " SHOWDOWN " + "="*20)
    score_j, texte_j = Evaluateur.evaluer(joueur.main + board)
    score_b, texte_b = Evaluateur.evaluer(bot.main + board)

    print(f"Tes cartes : {joueur.main} -> {texte_j}")
    print(f"Bot cartes : {bot.main} -> {texte_b}")

    if score_j > score_b:
        print("\n🏆 FÉLICITATIONS, TU AS GAGNÉ !")
    elif score_j < score_b:
        print("\n🤖 DOMMAGE, LE BOT ÉTAIT PLUS FORT.")
    else:
        print("\n🤝 ÉGALITÉ !")

if __name__ == "__main__":
    duel_poker()
