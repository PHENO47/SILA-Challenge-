

# 🌸 Iris Species Classifier : Pipeline ML Hybride (Jour 8)

Ce projet réalise une implémentation complète d'un pipeline de **Machine Learning "End-to-End"**. L'objectif est de classifier les espèces de fleurs d'Iris avec une précision maximale tout en garantissant l'interprétabilité du modèle et la portabilité du code.

## 🌟 Points Forts du Projet

* **Architecture Hybride** : Détection automatique de l'environnement. Le script affiche les graphiques sur **PC** et les exporte automatiquement en `.png` sur **Mobile (Pydroid 3)** pour éviter les plantages d'interface.
* **Pipeline Scikit-Learn** : Intégration du `StandardScaler` et du `RandomForestClassifier` dans un seul objet pour éviter le *Data Leakage*.
* **Optimisation des Hyperparamètres** : Utilisation de `GridSearchCV` pour trouver la meilleure configuration du modèle.
* **Interprétabilité** : Analyse de l'importance des variables pour comprendre les critères de décision de l'IA.
* **Persistance** : Exportation du modèle final au format `.joblib` pour une utilisation future sans réentraînement.

---

## 📊 Analyse des Performances

### 1. Matrice de Confusion

La matrice de confusion permet de visualiser la qualité des prédictions pour les trois classes : *Setosa*, *Versicolor*, et *Virginica*.

* **Diagonale principale** : Indique les bonnes prédictions.
* **Hors-diagonale** : Indique les erreurs de classification.

### 2. Importance des Variables (Feature Importance)

L'analyse montre quelles mesures physiques sont les plus déterminantes. Généralement, la **largeur du pétale** (`petal width`) est le prédicteur le plus puissant pour ce dataset.

---

## 🛠️ Guide d'Utilisation

### Installation des dépendances

```bash
pip install pandas matplotlib scikit-learn joblib

```

### Structure des fichiers générés

Après exécution, le projet génère les fichiers suivants dans votre dossier :

* 📄 `iris_model_final.joblib` : Le modèle entraîné prêt à l'emploi.
* 🖼️ `confusion_matrix.png` : Rapport visuel des erreurs/succès.
* 🖼️ `feature_importance.png` : Graphique d'interprétabilité des données.

### Navigation dans les graphiques (Mobile)

Si vous visualisez les graphiques sur Pydroid 3 :

* **Icône Disquette** : Sauvegarder manuellement l'image.
* **Icône Maison** : Réinitialiser la vue après un zoom.
* **Fermeture (X)** : Nécessaire pour passer au graphique suivant dans le script.

---

## 🔬 Détails Techniques

| Composant | Technologie |
| --- | --- |
| **Dataset** | Iris (Scikit-Learn Built-in) |
| **Prétraitement** | StandardScaler (Z-score normalization) |
| **Modèle** | Random Forest (Ensemble Learning) |
| **Validation** | Cross-Validation (CV=3) |
| **Interface** | Matplotlib avec gestion d'exceptions (`Agg` backend) |


## ✍️ Auteur

**PHENO47** 
