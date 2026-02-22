♠️ Texas Hold'em Simulator & AI - Jour 5
Bienvenue dans le projet du Jour 5 ! Ce défi marque une étape importante dans la maîtrise de la Programmation Orientée Objet (POO) en simulant un moteur de jeu de Poker interactif contre une Intelligence Artificielle.

🎯 Objectifs du Challenge
L'objectif était de construire un moteur de jeu robuste capable de :

Modéliser les entités physiques (Cartes, Deck, Joueurs) via des classes.

Évaluer mathématiquement la force des combinaisons de cartes.

Prédire les chances de victoire en utilisant des simulations statistiques.

Créer une boucle de jeu interactive Homme vs Machine.

🚀 Fonctionnalités Clés
🧠 Intelligence Artificielle (Monte-Carlo)
Plutôt que d'utiliser des probabilités figées, l'IA et l'assistant du joueur utilisent une Simulation de Monte-Carlo.

À chaque étape (Flop, Turn, River), le script simule 300 fins de parties possibles avec les cartes restantes dans le deck.

Il calcule ainsi un pourcentage de victoire dynamique pour aider l'utilisateur et permettre au Bot de prendre des décisions (Suivre ou se Coucher).

🃏 Moteur d'Évaluation
Un algorithme analyse les 7 cartes disponibles (2 privées + 5 communes) pour identifier la meilleure main possible :

Du simple "Carte Haute" à la redoutable "Quinte Flush".

Utilisation de la classe collections.Counter pour une analyse fréquentielle rapide des paires, brelans et carrés.

🎮 Gameplay Interactif
Le jeu se déroule en temps réel dans le terminal avec un affichage ASCII :

Distribution : Vous recevez vos cartes privées.

Enchères par étapes : Des tours de décision après le Flop, la Turn et la River.

Bot Stratégique : Le Bot analyse ses propres chances. Si ses probabilités de gain tombent sous les 15%, il abandonne la partie.

🛠️ Architecture du Code (POO)
Le projet est structuré autour de quatre classes principales :

Carte : Définit la valeur et l'enseigne (♥, ♦, ♣, ♠).

Deck : Gère le mélange et la distribution du sabot de 52 cartes.

Evaluateur : Contient la logique métier pure pour le calcul des scores.

Joueur : Gère l'état du joueur (main, jetons, type de décision).

📥 Installation et Test
Clonez le dépôt.

Lancez le script sans aucune dépendance externe :

Bash

python main.py
✍️ Auteur
PHENO47 - Explorateur de données et développeur Python.

💡 Ce que j'ai appris aujourd'hui
La puissance de la POO pour organiser des systèmes complexes.

L'utilisation de simulations aléatoires pour résoudre des problèmes probabilistes difficiles.

La gestion des flux d'interaction utilisateur (input) synchronisés avec une logique de Bot.
