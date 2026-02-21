# 🚀 Data Engineering ETL Pipeline Project

## 📌 Project Overview

This project implements a complete **ETL (Extract – Transform – Load) pipeline** using Python.

It processes multiple datasets:

- Titanic
- Iris
- Amazon
- Weather

The pipeline performs:

✅ Data Extraction  
✅ Data Cleaning  
✅ Feature Engineering  
✅ Outlier Detection  
✅ Data Scaling  
✅ Visualization  
✅ Data Export (CSV + Excel)  
✅ Dataset Merging  

---

## 🏗 Project Architecture


Extract → Transform → Load → Visualization → Export


The processed datasets are stored inside the `outputs/` folder.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- XlsxWriter

---

## 📂 Project Structure


Data-Engineering-Project/
│
├── data/
├── outputs/
├── etl_pipeline.py
├── requirements.txt
└── README.md


---

## ▶ How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Run the pipeline
python etl_pipeline.py
3. Check results

Generated files will be stored inside:

outputs/
🔥 Features Implemented

Handling missing values using median imputation

Outlier detection using IQR method

Feature creation (mean, std, median)

Data scaling using StandardScaler

Automatic dataset export (CSV + Excel)

Automated visualization

Dataset merging

👨‍💻 Author

PHENO47
University of Yaoundé I
