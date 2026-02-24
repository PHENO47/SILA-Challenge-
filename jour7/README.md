💱 Currency Master Ultimate (v1.2) - Jour 7

Bienvenue dans le projet final de la Semaine 1. Ce convertisseur de devises n'est pas un simple script de calcul ; c'est une application robuste conçue pour gérer les problématiques réelles du web : latence réseau, limites d'API et expérience utilisateur.

🚀 Fonctionnalités Clés
Intelligence Réseau (Retry Exponentiel) : 
En cas d'échec de l'API, le script retente la connexion en doublant le temps d'attente entre chaque essai (2s, 4s, 8s).

Cache SQLite (Performance) : Les taux sont stockés localement avec un TTL (Time To Live) de 10 minutes pour éviter les appels inutiles et accélérer l'application.

Assistance UX : Module intégré pour lister dynamiquement les codes de devises supportés (USD, EUR, XAF, etc.).

Visualisation de Données : Génération d'un graphique d'évolution sur 30 jours exporté automatiquement au format .png.

Conformité Mobile : Configuration spécifique pour un affichage optimal sur Pydroid 3.

🛠️ Architecture du Code
Le script est divisé en 5 modules logiques :

Base de Données : Initialise SQLite pour la persistance.

Couche Réseau : Gère les requêtes requests avec la logique de résilience.

Aide Utilisateur : Parse les données de l'API pour extraire les codes disponibles.

Module Graphique : Utilise Matplotlib pour transformer les données brutes en visuel exploitable.

Moteur Principal : Coordonne les entrées utilisateur et les calculs.

📖 Guide d'Utilisation

1. Installation des dépendance

Avant de lancer le script, installez les bibliothèques nécessaires :

Bash

pip install requests matplotlib
2. Lancement

Exécutez le script depuis votre terminal ou Pydroid 3 :

Bash

python main.py


3. Étapes d'utilisation

Aide au choix : Au démarrage, tapez o si vous ne connaissez pas le code ISO de votre devise (ex: XAF pour le Franc CFA).

Saisie : Entrez la devise source, la cible et le montant.

Résultat : Le script affiche instantanément la conversion et le taux actuel.

Graphique : Tapez o pour générer le visuel. Le fichier evolution_devises.png sera créé dans votre dossier.

📊 Pourquoi l'usage de SQLite et Matplotlib ?
SQLite : Permet de garder l'application fonctionnelle même avec une connexion instable si les taux ont déjà été mis en cache.

Matplotlib : Apporte une valeur ajoutée professionnelle en permettant d'analyser les tendances au-delà d'un simple chiffre statique.

✍️ Auteur
PHENO47 - Challenge 30 Jours de Python (Semaine 1 complétée).

