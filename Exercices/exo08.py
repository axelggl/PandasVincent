# Supposez que vous avez un autre DataFrame df_promotions avec les colonnes Date, Magasin, et Promotion. Effectuez une jointure avec df pour lier les données de promotions aux ventes.

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
df_promotions = pd.read_csv('donnees_promotions.csv')
df_merged = pd.merge(df, df_promotions, on=['Date', 'Magasin'], how='left')
print("==== Données fusionnées ====")
print(df_merged) # Affiche les données fusionnées