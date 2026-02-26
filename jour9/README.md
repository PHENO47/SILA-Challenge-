
#  Kanban Ultimate Pro – Gestionnaire de Tâches Avancé (PyQt6)

## 📌 Description

**Kanban Ultimate Pro** est une application développée en **Python avec PyQt6**, permettant de gérer des tâches via une interface **Kanban moderne** avec :

* Colonnes dynamiques (À faire / En cours / Terminé)
* Drag & Drop fonctionnel
* Système de priorité et de tags
* Filtres dynamiques
* Persistance SQLite avec migration automatique
* Notifications système
* Export CSV et PDF

Projet réalisé dans le cadre d’un challenge :
**Gestionnaire de Tâche Avancé PyQt**


## 🖥 Aperçu des fonctionnalités

### 🎯 Vue Kanban interactive

* 3 colonnes : À faire / En cours / Terminé
* Déplacement des tâches par Drag & Drop
* Mise à jour automatique du statut en base SQLite


### 🏷 Gestion avancée des tâches

* Priorité : Basse / Moyenne / Haute
* Tags personnalisables
* Recherche dynamique par titre ou tag
* Filtre par priorité


### 💾 Persistance des données

* Base de données locale SQLite
* Création automatique du schéma
* Sauvegarde persistante des tâches


### 🔔 Notifications système

* Notification automatique lors de l’ajout d’une nouvelle tâche
* Intégration via `QSystemTrayIcon`


### 📊 Export des données

* Export complet en CSV
* Génération automatique d’un rapport PDF


## 🛠 Technologies utilisées

* Python 3.9+
* PyQt6
* SQLite3
* CSV (standard library)
* Qt Print Support


## 📦 Installation

1️⃣ Cloner le dépôt :

```bash
git clone https://github.com/PHENO47/kanban-ultimate-pro.git
cd kanban-ultimate-pro
```

2️⃣ Installer les dépendances :

```bash
pip install PyQt6
```

3️⃣ Lancer l’application :

```bash
python main.py
```

---

## 📁 Structure du projet

```
kanban-ultimate-pro/
│
├── main.py
├── kanban_ultimate.db (créé automatiquement)
├── kanban_export.csv (généré à l’export)
├── kanban_report.pdf (généré à l’export)
└── README.md
```

---

## 🧠 Architecture

Le projet est structuré en trois parties principales :

* `Database` : Gestion SQLite et migration automatique
* `KanbanList` : Composant personnalisé avec gestion Drag & Drop
* `KanbanApp` : Interface principale et logique métier

---

## 🚀 Fonctionnalités validées dans le challenge

* ✔ Vue Kanban avec Drag & Drop
* ✔ Tags + Priorité + filtres dynamiques
* ✔ Persistance SQLite avec migration
* ✔ Notifications système
* ✔ Export CSV / PDF

---

## 📌 Améliorations possibles

* Édition de tâche (double clic)
* Suppression via menu contextuel
* Dashboard avec statistiques
* Icône personnalisée
* Packaging en .exe (PyInstaller)

---

## 👨‍💻 Auteur: PHENO47

Projet développé dans le cadre d’un challenge Python / PyQt6
Objectif : démonstration de compétences en développement d’application desktop.

---
