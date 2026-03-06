# 🤖 Bot d’Automatisation Web avec Selenium

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

Bot de **scraping web automatisé** développé en **Python** utilisant **Selenium** pour interagir avec des pages web dynamiques, **BeautifulSoup** pour l'extraction structurée des données et **SQLite** pour le stockage local.

Le bot inclut plusieurs mécanismes pour imiter un comportement humain et éviter les blocages simples :

* rotation du **User-Agent**
* **délais aléatoires**
* gestion des **cookies**
* interaction avec **contenu AJAX**
* **scraping programmé automatiquement** avec APScheduler

---

# 📌 Fonctionnalités

✔ Scraping web automatisé avec **Selenium**
✔ Support des **sites dynamiques (JavaScript / AJAX)**
✔ Rotation de **User-Agent** pour réduire la détection bot
✔ Délais aléatoires entre les actions
✔ Extraction structurée avec **BeautifulSoup**
✔ Stockage des données dans **SQLite**
✔ Export automatique en **CSV**
✔ Lancement périodique du bot avec **APScheduler**
✔ Interface simple : l'utilisateur entre juste **l'URL à scraper**

---

# 🗂 Structure du Projet

```
bot-automation-selenium/
│
├── bot/
│   ├── scraper.py
│   ├── parser.py
│   ├── database.py
|   ├── scheduler.py
|   ├── utils.py
│
├── data/
│   ├── scraped_data.db
│   └── export.csv
│

├── main.py
├── requirements.txt
└── README.md
```

### Description des fichiers

| Fichier        | Rôle                                      |
| -------------- | ----------------------------------------- |
| `main.py`      | Point d'entrée du programme               |
| `scheduler.py` | Planifie l'exécution périodique du bot    |
| `scraper.py`   | Gestion du navigateur Selenium            |
| `parser.py`    | Extraction des données avec BeautifulSoup |
| `database.py`  | Enregistrement dans SQLite                |
| `data/`        | Contient les données récupérées           |

---

# ⚙️ Installation

## 1️⃣ Cloner le projet

```
git clone https://github.com/PHENO47/SILA-Challenge.git
cd jour14
```

---

## 2️⃣ Installer les dépendances

```
pip install -r requirements.txt
```

---

## 3️⃣ Installer ChromeDriver

Télécharger :

https://chromedriver.chromium.org/downloads

Puis placer **chromedriver** dans :

```
bot/
```

---

# 📦 requirements.txt

```
selenium
beautifulsoup4
pandas
apscheduler
```

---

# 🚀 Lancer le bot

Exécuter :

```
python main.py
```

Le programme demandera :

```
=== BOT AUTOMATISATION WEB ===

Entrer l'URL du site à scraper :
```

Exemple :

```
https://quotes.toscrape.com/js/
```

Puis l'intervalle :

```
Intervalle de scraping (minutes) :
```

Exemple :

```
5
```

Le bot exécutera alors un scraping **toutes les 5 minutes**.

---

# 🧠 Comment fonctionne le bot

## 1️⃣ L'utilisateur entre une URL

Le programme demande l'adresse du site :

```
Entrer l'URL du site à scraper :
```

---

## 2️⃣ Selenium ouvre le navigateur

Le bot lance **Chrome en mode automatisé**.

Exemple :

```
[INFO] Ouverture du navigateur
[INFO] Chargement de la page
```

---

## 3️⃣ Simulation d'un comportement humain

Le bot applique :

* User-Agent aléatoire
* délai aléatoire

Exemple :

```
[INFO] Attente aléatoire : 3.2 secondes
```

---

## 4️⃣ Récupération du HTML

Selenium charge entièrement la page, y compris le contenu **JavaScript / AJAX**.

---

## 5️⃣ Extraction des données

BeautifulSoup analyse le HTML :

```python
soup = BeautifulSoup(html, "html.parser")
quotes = soup.find_all("span", class_="text")
```

Exemple de données récupérées :

| Quote                     |
| ------------------------- |
| "Life is what happens..." |
| "Be yourself..."          |

---

## 6️⃣ Stockage des données

Les données sont sauvegardées dans :

```
data/scraped_data.db
```

Structure de la table :

```
quotes
```

| id | quote    |
| -- | -------- |
| 1  | citation |
| 2  | citation |

---

## 7️⃣ Export CSV

Les données sont aussi exportées dans :

```
data/export.csv
```

---

## 8️⃣ Scheduler automatique

APScheduler relance le scraping selon l'intervalle choisi.

Exemple :

```
Bot lancé : scraping toutes les 5 minutes
```

Logs :

```
Scraping en cours...
Données trouvées : 10
```

---

# 📊 Exemple d'exécution

```
=== BOT AUTOMATISATION WEB ===

Entrer l'URL du site à scraper :
https://quotes.toscrape.com/js/

Intervalle de scraping (minutes) :
5

Bot lancé : scraping toutes les 5 minutes

Scraping en cours...
Données trouvées : 10
```

---

# 🌍 Sites recommandés pour tester

### Quotes

```
https://quotes.toscrape.com/js/
```

### Books

```
https://books.toscrape.com/
```

---

# 📈 Améliorations possibles

* Proxy rotatif
* Interface graphique
* Scraping multi-sites
* Export JSON
* Dashboard de visualisation
* Déploiement sur serveur

---

# 📜 Licence

Projet open source sous licence **MIT**.

---

# 👨‍💻 Auteur
**PHENO47**

Projet réalisé dans le cadre d'un **SILA CHALLENGE / Web Scraping**.
