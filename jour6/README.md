🕹️ Platformer Pro Hybrid - Jour 6
Bienvenue dans le projet phare du Jour 6 ! Ce défi a consisté à développer un moteur de jeu de plateforme 2D complet, capable de fonctionner nativement sur PC (clavier) et sur Mobile (tactile via Pydroid 3).

🌟 Fonctionnalités Principales
Moteur Physique "Custom" : Gestion manuelle des vecteurs de mouvement, de la gravité, de la friction et des rebonds élastiques.

Contrôles Hybrides :

PC : Flèches directionnelles, Espace (Saut) et Ctrl (Tir).

Mobile : Système de zones tactiles invisibles (Gauche, Saut central, Droite).

Architecture de Niveau (Data-Driven) : Chargement des plateformes, ennemis et objets via un fichier externe map.json.

Intelligence Artificielle : Ennemis dotés d'un double comportement (Patrouille simple ou Poursuite active du joueur).

Système de Score : Collecte de pièces et sauvegarde persistante du High Score dans un fichier highscore.txt.

🏗️ Architecture Technique
1. Collisions AABB (Axis-Aligned Bounding Box)
Pour éviter que le joueur ne traverse les murs ou le sol, le moteur utilise une détection de collision séparée sur les deux axes (X et Y). Cela garantit une précision parfaite lors des sauts et des déplacements latéraux.

2. Le Pipeline de Données (JSON)
Le jeu sépare strictement la logique (Python) du design du niveau (JSON). Voici un exemple de la structure utilisée :

JSON

{
  "platforms": [{"x": 0, "y": 410, "w": 800, "h": 40}],
  "enemies": [{"x": 450, "y": 150}],
  "coins": [{"x": 160, "y": 270}]
}
3. Intelligence Artificielle
L'IA calcule en permanence la distance relative entre l'ennemi et le joueur. Si le joueur entre dans le detection_range, l'ennemi change son mode de patrouille pour un mode "Chasseur".

🎮 Comment Jouer ?
Sur Ordinateur 💻
Action	Touche
Se déplacer	Flèches Gauche / Droite
Sauter	Espace
Tirer	Ctrl Gauche

Sur Pydroid 3 (Mobile) 📱
L'écran est divisé en 3 zones invisibles :

Tiers Gauche : Déplacement vers la gauche.

Tiers Central : Sauter.

Tiers Droit : Déplacement vers la droite.

Zone Supérieure : Tirer un projectile.

🛠️ Installation
Prérequis : Assurez-vous d'avoir Python et la bibliothèque Pygame.

Bash

pip install pygame
Fichiers nécessaires :

main.py (le code source)

map.json (la structure du niveau)

Lancement :

Bash

python main.py
✍️ Auteur
PHENO47 