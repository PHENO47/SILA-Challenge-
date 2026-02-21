import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# ==============================
# 1️⃣ EXTRACT
# ==============================

def extract():
    print("🔍 Extraction des données...")
    
    titanic = pd.read_csv("data/titanic.csv")
    iris = pd.read_csv("data/iris.csv")
    amazon = pd.read_csv("data/amazon.csv")
    weather = pd.read_csv("data/weather.csv")
    
    return titanic, iris, amazon, weather


# ==============================
# 2️⃣ TRANSFORM
# ==============================

def clean_missing_values(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    
    return df


def detect_outliers_iqr(df, column):
    if column not in df.columns:
        return None
    
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower) | (df[column] > upper)]
    
    print(f"⚠️ Outliers détectés dans {column} : {len(outliers)}")
    
    return outliers


def create_features(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    if len(numeric_cols) > 0:
        df["mean_all"] = df[numeric_cols].mean(axis=1)
        df["std_all"] = df[numeric_cols].std(axis=1)
        df["median_all"] = df[numeric_cols].median(axis=1)
    
    return df


def scale_numeric(df):
    from sklearn.preprocessing import StandardScaler
    
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    if len(numeric_cols) == 0:
        print("⚠️ Aucune colonne numérique à normaliser.")
        return df
    
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df


# ==============================
# 3️⃣ LOAD
# ==============================

def export_data(df, name):
    df.to_csv(f"outputs/{name}_processed.csv", index=False)
    
    with pd.ExcelWriter(f"outputs/{name}_report.xlsx", engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Cleaned Data", index=False)
        
        workbook = writer.book
        worksheet = writer.sheets["Cleaned Data"]
        
        header_format = workbook.add_format({
            "bold": True,
            "bg_color": "#D7E4BC",
            "border": 1
        })
        
        for col_num, value in enumerate(df.columns):
            worksheet.write(0, col_num, value, header_format)


# ==============================
# VISUALISATION
# ==============================

def visualize(df, name):
    plt.figure(figsize=(10,5))
    
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    if len(numeric_cols) > 0:
        sns.histplot(df[numeric_cols[0]], kde=True)
        plt.title(f"Distribution - {name}")
        plt.savefig(f"{name}_plot.png")
        plt.show()


# ==============================
# PIPELINE PRINCIPAL
# ==============================

def etl_pipeline():
    #creation du dossier output si absent
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    titanic, iris, amazon, weather = extract()

    datasets = {
        "titanic": titanic,
        "iris": iris,
        "amazon": amazon,
        "weather": weather
    }
    
    processed_data = []
    
    for name, df in datasets.items():
        
        print(f"\n🔄 Traitement : {name}")
        
        df = clean_missing_values(df)
        df = create_features(df)
        df = scale_numeric(df)
        
        numeric_cols = df.select_dtypes(include=np.number).columns
        if len(numeric_cols) > 0:
           detect_outliers_iqr(df, numeric_cols[0])
        
        visualize(df, name)
        export_data(df, name)
        
        processed_data.append(df)
    
    # Fusion globale
    final_dataset = pd.concat(processed_data, axis=0, ignore_index=True)
    final_dataset.to_csv("outputs/final_merged_dataset.csv", index=False)
    
    print("\n✅ Pipeline ETL terminé avec succès !")


if __name__ == "__main__":
    etl_pipeline()
