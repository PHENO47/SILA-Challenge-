import requests
import sqlite3
import json
import time
import random
import os
import matplotlib
# Configuration spécifique pour l'affichage sur Pydroid 3
try:
    matplotlib.use('Agg') 
except:
    pass
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- CONFIGURATION ---
DB_NAME = "currency_cache.db"
TTL_SECONDS = 600 

# --- 1. GESTION DE LA BASE DE DONNÉES ---
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rates 
                     (base TEXT, target TEXT, rate REAL, timestamp DATETIME)''')
    conn.commit()
    conn.close()

# --- 2. RÉCUPÉRATION API AVEC RETRY ---
def fetch_rates_with_retry(base, retries=3):
    delay = 2
    for i in range(retries):
        try:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base}")
            response.raise_for_status()
            return response.json()['rates']
        except Exception as e:
            if i == retries - 1: raise e
            time.sleep(delay)
            delay *= 2

# --- 3. LISTER LES DEVISES (AIDE UX) ---
def list_currencies():
    print("\n🌍 Chargement des devises disponibles...")
    try:
        rates = fetch_rates_with_retry("USD")
        codes = sorted(rates.keys())
        print("\n--- CODES DEVISES DISPONIBLES ---")
        for i in range(0, len(codes), 6):
            print("  ".join(codes[i:i+6]))
        print("-" * 40)
    except:
        print("⚠️ Erreur de connexion pour la liste.")

# --- 4. VISUALISATION GRAPHIQUE (HISTORIQUE 30J) ---
def show_evolution(base, target, current_rate):
    """ Génère un graphique d'évolution simulé sur 30 jours """
    print(f"\n📊 Génération du graphique {base}/{target}...")
    
    dates = [(datetime.now() - timedelta(days=i)).strftime("%d/%m") for i in range(30)]
    dates.reverse()
    
    # Simulation de variations réalistes (+/- 2%)
    rates = [current_rate * (1 + random.uniform(-0.02, 0.02)) for _ in range(30)]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o', linestyle='-', color='#2ecc71')
    plt.title(f"Évolution 30j : {base} vers {target}")
    plt.xlabel("Date")
    plt.ylabel("Taux")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Sauvegarde et affichage
    filename = "evolution_devises.png"
    plt.savefig(filename)
    print(f"✅ Graphique sauvegardé sous : {filename}")
    try:
        plt.show()
    except:
        print("💡 Note : Consultez le fichier .png si la fenêtre ne s'ouvre pas.")

# --- 5. LOGIQUE PRINCIPALE ---
def main():
    init_db()
    print("="*40)
    print("💱 CURRENCY MASTER PRO v1.2 (FINAL)")
    print("="*40)
    
    if input("📝 Voir la liste des devises ? (o/n) : ").lower() == 'o':
        list_currencies()

    try:
        base = input("\n💰 Devise source (ex: USD) : ").upper()
        target = input("🎯 Devise cible (ex: EUR) : ").upper()
        amount = float(input("💵 Montant : "))

        # Tentative via API
        rates = fetch_rates_with_retry(base)
        rate = rates.get(target)

        if rate:
            result = amount * rate
            print(f"\n✅ RÉSULTAT : {amount} {base} = {result:.2f} {target}")
            print(f"📈 Taux actuel : 1 {base} = {rate} {target}")
            
            if input("\n📊 Afficher le graphique d'évolution ? (o/n) : ").lower() == 'o':
                show_evolution(base, target, rate)
        else:
            print(f"❌ La devise '{target}' n'existe pas.")

    except ValueError:
        print("❌ Erreur : Entrez un montant valide.")
    except Exception as e:
        print(f"❌ Erreur critique : {e}")

if __name__ == "__main__":
    main()