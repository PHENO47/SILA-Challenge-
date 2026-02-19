import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# 1. CHARGEMENT ET STATISTIQUES
# Utilisation du dataset intégré pour éviter les erreurs de chemin de fichier
df = sns.load_dataset('iris')

print("--- STATISTIQUES DESCRIPTIVES ---")
stats = df.describe()
print(stats)
print("\n---------------------------------\n")

# 2. CONFIGURATION DE LA FIGURE
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Tableau de Bord Iris - Challenge Jour 2', fontsize=18, fontweight='bold')

# --- GRAPHIQUE 1 : HISTOGRAMME (Top Left) ---
sns.histplot(df['sepal_length'], kde=True, ax=axes[0, 0], color="royalblue")
axes[0, 0].set_title('Distribution : Longueur Sépale', fontsize=12)
axes[0, 0].set_xlabel('Longueur (cm)')

# --- GRAPHIQUE 2 : SCATTER PLOT + RÉGRESSION (Top Right) ---
sns.regplot(data=df, x='sepal_length', y='petal_length', ax=axes[0, 1], 
            scatter_kws={'alpha':0.5, 'color':'teal'}, line_kws={'color':'red'})
axes[0, 1].set_title('Corrélation Sépale vs Pétale', fontsize=12)
axes[0, 1].annotate('Forte corrélation', xy=(5, 2), xytext=(6, 1),
                     arrowprops=dict(facecolor='black', shrink=0.05))

# --- GRAPHIQUE 3 : HEATMAP DE CORRÉLATION (Bottom Left) ---
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu', ax=axes[1, 0], cbar=False)
axes[1, 0].set_title('Matrice de Corrélation', fontsize=12)

# --- GRAPHIQUE 4 : COURBE ANIMÉE (Bottom Right) ---
# Préparation des données pour l'animation
x_data = []
y_data = []
line, = axes[1, 1].plot([], [], lw=2, color='darkorange', marker='o', markevery=[-1])
axes[1, 1].set_xlim(0, 50)
axes[1, 1].set_ylim(df['petal_width'].min(), df['petal_width'].max())
axes[1, 1].set_title('Animation : Largeur Pétale (Live)', fontsize=12)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x_data.append(frame)
    y_data.append(df['petal_width'].iloc[frame])
    line.set_data(x_data, y_data)
    return line,

# Création de l'animation (50 premiers points)
ani = FuncAnimation(fig, update, frames=range(50), init_func=init, blit=True, interval=100, repeat=False)

# Ajustement final de la mise en page
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
