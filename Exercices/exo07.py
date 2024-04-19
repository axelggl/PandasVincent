# Triez le DataFrame par date de vente en ordre décroissant. Classez les magasins selon le revenu total en ordre décroissant

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire'] # Crée une nouvelle colonne Revenu en multipliant les colonnes Quantité vendue et Prix unitaire
df['Année'] = pd.to_datetime(df['Date']).dt.year # Crée une nouvelle colonne Année en extrayant l'année de la colonne Date
df = df.sort_values('Date', ascending=False) # Trie le DataFrame par date de vente en ordre décroissant
magasins_revenu_total = df.groupby('Magasin')['Revenu'].sum().sort_values(ascending=False) # Classe les magasins selon le revenu total en ordre décroissant
print("==== DataFrame trié par date de vente ====")
print(df)
print("==== Magasins classés selon le revenu total ====")
print(magasins_revenu_total) # Affiche les magasins classés selon le revenu total