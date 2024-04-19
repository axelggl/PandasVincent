# Calculez le total des revenus par magasin. Trouvez le produit le plus vendu.

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire'] # Crée une nouvelle colonne Revenu en multipliant les colonnes Quantité vendue et Prix unitaire
total_revenus_par_magasin = df.groupby('Magasin')['Revenu'].sum() # Calcule le total des revenus par magasin
produit_plus_vendu = df.groupby('Produit')['Quantité vendue'].sum().idxmax() # Trouve le produit le plus vendu
print("==== Total des revenus par magasin ====")
print(total_revenus_par_magasin) # Affiche le total des revenus par magasin
print("==== Produit le plus vendu ====")
print(produit_plus_vendu) # Affiche le produit le plus vendu