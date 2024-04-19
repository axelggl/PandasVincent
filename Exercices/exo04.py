# Ajoutez une nouvelle colonne Revenu qui est le produit de Quantité vendue par Prix unitaire. Créez une colonne Année extraite de la colonne Date.

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire'] # Crée une nouvelle colonne Revenu en multipliant les colonnes Quantité vendue et Prix unitaire
df['Année'] = pd.to_datetime(df['Date']).dt.year # Crée une nouvelle colonne Année en extrayant l'année de la colonne Date
print(df.describe())
