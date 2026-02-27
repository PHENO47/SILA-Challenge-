
# 🎮 Morpion IA – Minimax Alpha-Beta (N×N)

> Jeu de Morpion intelligent développé en Python (POO) avec interface graphique Pygame et IA basée sur l’algorithme Minimax optimisé par élagage Alpha-Beta.

---

## 🚀 Aperçu du projet

Ce projet implémente un **jeu de Morpion extensible (grille N×N)** avec :

* 🤖 IA Minimax + Alpha-Beta
* 🎯 3 niveaux de difficulté (Facile / Moyen / Impossible)
* 👥 Mode deux joueurs local
* 🖥 Interface graphique animée avec Pygame
* 🏆 Score conservé entre les parties
* 🔁 Boutons Rejouer / Quitter
* 📝 Enregistrement des parties en notation algébrique

---

## 🧠 Intelligence Artificielle

L’IA repose sur :

* Algorithme **Minimax**
* Élagage **Alpha-Beta pruning**
* Priorisation des coups centraux (optimisation)
* Heuristique dépendante de la profondeur
* Limitation de profondeur (niveau moyen)

### 🎚 Niveaux

| Niveau     | Comportement                    |
| ---------- | ------------------------------- |
| Easy       | Coup aléatoire                  |
| Medium     | Minimax avec profondeur limitée |
| Impossible | Minimax complet + Alpha-Beta    |

---

## 🏗 Architecture du projet

```
morpion-ai/
│
├── main.py        # Point d'entrée
├── game.py        # Orchestration globale
├── board.py       # Logique du plateau
├── ai.py          # Intelligence artificielle
├── renderer.py    # Affichage Pygame
├── recorder.py    # Enregistrement des coups
├── config.py      # Constantes globales
└── README.md
```

### 🔥 Séparation propre des responsabilités

* **Board** → logique pure
* **AI** → algorithme décisionnel
* **Renderer** → affichage uniquement
* **Game** → coordination
* **Recorder** → sauvegarde

Architecture pensée pour être :

* Maintenable
* Extensible
* Lisible pour un jury technique

---

## 🖥 Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/PHENO47/silla-challenge.git
cd silla-challenge/jour10
python main.py
```

### 2️⃣ Installer dépendances

```bash
pip install pygame
```

### 3️⃣ Lancer le jeu

```bash
python main.py
```

---

## 🎮 Fonctionnalités

### ✔ Interface graphique

* Grille dynamique N×N
* Overlay de fin
* Boutons interactifs
* Affichage du score

### ✔ Score persistant

Le score est conservé tant que le programme tourne :

```
Score  X : 2  |  O : 1
```

### ✔ Rejouer / Quitter

Après chaque partie :

* 🎉 Message de victoire
* 🔁 Bouton Rejouer
* ❌ Bouton Quitter

### ✔ Sauvegarde automatique

Les coups sont enregistrés en notation algébrique :

```
1. X A1
2. O B2
3. X C1
...
```

---

## 📈 Performances

L’optimisation Alpha-Beta réduit drastiquement le nombre de noeuds explorés.

* Complexité Minimax brute : O(b^d)
* Avec Alpha-Beta : réduction significative (≈ moitié dans le meilleur cas)

---

## 🧩 Extensibilité

Le jeu supporte une grille N×N :

Dans `config.py` :

```python
DEFAULT_BOARD_SIZE = 3
```

Tu peux tester :

```python
DEFAULT_BOARD_SIZE = 4
DEFAULT_BOARD_SIZE = 5
```

⚠ Pour N > 3, le niveau "Impossible" peut être plus lent (complexité exponentielle).

---

## 📚 Concepts techniques utilisés

* Programmation Orientée Objet (POO)
* Algorithmes de recherche
* Récursion
* Heuristiques
* Optimisation Alpha-Beta
* Architecture modulaire
* Gestion d’événements (Pygame)

---

## 🏆 Objectif pédagogique

Ce projet vise à :

* Comprendre Minimax
* Implémenter Alpha-Beta
* Structurer un projet proprement
* Séparer logique / rendu
* Créer une IA déterministe

---

## 🚀 Améliorations futures

* Animation ligne gagnante
* Effets sonores
* Sauvegarde score en JSON
* Transposition table
* Interface menu avancée
* Mode multijoueur réseau
* Interface mobile optimisée

---

## 👨‍💻 Auteur

PHENO47 
Développeur Python | Passionné IA & Cybersécurité

---

