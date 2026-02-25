import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay, classification_report

# --- FONCTION D'AFFICHAGE INTELLIGENTE ---
def smart_show(filename):
    """Affiche l'image sur PC ou la sauvegarde sur Mobile/Serveur."""
    try:
        # Tente d'afficher la fenêtre (OK sur PC)
        plt.tight_layout()
        plt.show()
        print(f"🖥️  Affichage écran réussi.")
    except Exception:
        # Si échec (Mobile/SSH), sauvegarde le fichier
        plt.savefig(filename)
        print(f"📱 Affichage impossible : Image sauvegardée sous '{filename}'")
    finally:
        plt.close()

print("🚀 Démarrage du Pipeline ML Hybride...")

# --- 1. CHARGEMENT ET PRÉPARATION ---
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 2. PIPELINE ET OPTIMISATION ---
pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [None, 5]
}

print("⚙️ Entraînement et recherche d'hyperparamètres...")
# n_jobs=1 pour la stabilité sur mobile, cv=3 pour la rapidité
grid_search = GridSearchCV(pipeline, param_grid, cv=3, n_jobs=1) 
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_

# --- 3. RAPPORT DE PERFORMANCE ---
y_pred = best_model.predict(X_test)
print("\n✅ Modèle optimisé !")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# --- 4. VISUALISATION 1 : MATRICE DE CONFUSION ---
print("\n📊 Génération de la Matrice de Confusion...")
fig, ax = plt.subplots(figsize=(8, 6))
ConfusionMatrixDisplay.from_estimator(best_model, X_test, y_test, 
                                      display_labels=iris.target_names, 
                                      cmap='viridis', ax=ax)
plt.title("Matrice de Confusion (Iris Dataset)")
smart_show("confusion_matrix.png")

# --- 5. VISUALISATION 2 : INTERPRÉTABILITÉ (Feature Importance) ---
print("🔍 Analyse de l'importance des variables...")
importances = best_model.named_steps['classifier'].feature_importances_
indices = np.argsort(importances)

plt.figure(figsize=(10, 5))
plt.title('Interprétabilité : Quelles mesures comptent le plus ?')
plt.barh(range(len(indices)), importances[indices], color='#3498db', align='center')
plt.yticks(range(len(indices)), [iris.feature_names[i] for i in indices])
plt.xlabel('Poids dans la décision')
smart_show("feature_importance.png")

# --- 6. EXPORT FINAL ---
joblib.dump(best_model, 'iris_model_final.joblib')
print(f"\n✨ TERMINÉ ! Modèle sauvegardé dans : {os.getcwd()}")