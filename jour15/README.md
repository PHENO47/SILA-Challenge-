Parfait 👍
On va faire un **README propre pour GitHub**, qui **garde le même style que tes précédents projets** (explication claire + badges + structure + utilisation), mais adapté à **la nouvelle version du jeu du pendu**.

Tu peux **copier-coller directement dans `README.md`**.

---

# 🪢 Hangman Game – Python Tkinter

```markdown
# 🪢 Hangman Game – Python Tkinter

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Game](https://img.shields.io/badge/Project-Hangman-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Un **jeu du pendu moderne développé en Python avec Tkinter**.  
Le joueur doit deviner un mot lettre par lettre avant que le pendu ne soit complètement dessiné.

Ce projet fait partie du **Silla Challenge** et inclut plusieurs améliorations modernes.

---

# 🎮 Fonctionnalités

✔ Interface graphique avec **Tkinter**  
✔ **Mode clair / sombre** au démarrage  
✔ **Score progressif** (+10 points par victoire)  
✔ **Clavier interactif**  
✔ Lettres **vertes si correctes**  
✔ Lettres **rouges si incorrectes**  
✔ **Mots chargés depuis un fichier externe**  
✔ **Nouvelle partie automatique**  
✔ **Système de dessin du pendu**

---

# 🖼 Aperçu du jeu

Le joueur doit deviner le mot :

```

_ _ _ _ _

```

Chaque mauvaise lettre ajoute une partie du pendu.

---

# 📂 Structure du projet

```

hangman-game
│
├── main.py          # Jeu principal
├── word_loader.py   # Chargement des mots
├── words.txt        # Liste des mots
└── README.md

```

---

# 📚 Fichier des mots

Les mots sont stockés dans :

```

words.txt

```

Exemple :

```

python
ordinateur
algorithme
developpeur
serveur

````

Le programme sélectionne un mot **aléatoire** à chaque partie.

---

# ⚙️ Installation

Clone le projet :

```bash
git clone https://github.com/PHENO47/SILA-Challenge.git
cd jour15
````

Entrer dans le dossier :

```bash
cd hangman-game
```

---

# ▶️ Lancer le jeu

Exécuter le programme :

```bash
python main.py
```

---

# 🎮 Comment jouer

1. Lancer le jeu
2. Choisir **mode clair ou sombre**
3. Deviner le mot en cliquant sur les lettres
4. Les couleurs indiquent le résultat :

```

🟩 Vert → bonne lettre
🟥 Rouge → mauvaise lettre

```

5. Si le mot est trouvé → **+10 points**

---

# 🧠 Technologies utilisées

* **Python**
* **Tkinter**
* **Programmation orientée objet**

---

# 🚀 Améliorations possibles

* Animation complète du pendu
* Leaderboard des scores
* Niveaux de difficulté
* Effets visuels
* Version mobile

---

# 👨‍💻 Auteur

Projet réalisé par **PHENO47** dans le cadre du **Sila Challenge**.

---
