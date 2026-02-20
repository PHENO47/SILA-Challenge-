🧮 jour3- Calculatrice Scientifique Tkinter
Bienvenue dans le troisième projet de mon challenge Python ! ce projet se concentre sur la création d'une interface graphique (GUI) complexe capable de traiter des expressions mathématiques avancées.

✨ Fonctionnalités Clés
Moteur d'Analyse Avancé : Support complet des parenthèses imbriquées et des priorités opératoires grâce à une intégration sécurisée de la bibliothèque math.

Fonctions Scientifiques implémenter sont: Trigonométrie (sin, cos, tan), logarithmes (log, ln), racine carrée (sqrt) et puissances (^).

Système de Thèmes : Basculement dynamique entre un Mode Sombre (optimisé pour la lecture) et un Mode Clair.

Persistance des Données : Sauvegarde automatique de l'historique des calculs dans un fichier local ,calcul_history.txt.

Interface Responsive : Mise en page dynamique utilisant la grille Tkinter, s'adaptant à toutes les tailles d'écran (Portrait/Paysage).

🛠️ Améliorations Techniques (Refactoring v2)
Ce code a été optimisé suite à une revue technique pour inclure :

Centralisation des Constantes : Couleurs et polices définies en début de fichier pour une maintenance.

Gestion Granulaire des Erreurs : Distinction entre les erreurs de syntaxe, les divisions par zéro et les entrées invalides via des blocs try/except.

Modularité : Séparation stricte entre la logique de calcul (safe_eval) et la gestion de l'interface graphique.

📥 Installation et Exécution
📱 Sur Mobile (Pydroid 3)
Vérification : Assurez-vous d'avoir le plugin Tcl/Tk display installé (disponible dans le Quick Install de Pydroid).

Copie : Enregistrez le fichier main.py dans votre stockage interne.

Lancement : Cliquez sur le bouton Play. L'interface s'ouvrira dans une fenêtre flottante.

💻 Sur Ordinateur (Windows / Mac / Linux)
Dépendances : Aucune bibliothèque externe n'est requise (Tkinter et Math font partie de la bibliothèque standard de Python).

Exécution :

Bash

python main.py
📂 Structure du dossier Jour 3
main.py : Code source de l'application.

calcul_history.txt : Fichier généré automatiquement contenant l'historique des opérations.

✍️ Auteur
PHENO47 - | Challenge 30 Jours 
