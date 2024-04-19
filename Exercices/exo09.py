# Exportez le DataFrame final en fichier CSV nommé resultats_ventes.csv

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire'] # Crée une nouvelle colonne Revenu en multipliant les colonnes Quantité vendue et Prix unitaire
df['Année'] = pd.to_datetime(df['Date']).dt.year # Crée une nouvelle colonne Année en extrayant l'année de la colonne Date
df_promotions = pd.read_csv('donnees_promotions.csv')
df_merged = pd.merge(df, df_promotions, on=['Date', 'Magasin'], how='left')
print("==== Données fusionnées ====")
print(df_merged) # Affiche les données fusionnées
df.to_csv('resultats_ventes.csv', index=False) # Exporte le DataFrame final en fichier CSV nommé resultats_ventes.csv
