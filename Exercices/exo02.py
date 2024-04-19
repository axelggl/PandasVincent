# Affichez les 5 premières lignes du DataFrame. Affichez le nombre de lignes et de colonnes du DataFrame. Affichez le type de chaque colonne.

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
print("==== 5 premières lignes ====")
print(df.head()) # Affiche les 5 premières lignes du DataFrame
print("==== Nombre de lignes et de colonnes ====")
print(df.shape) # Affiche le nombre de lignes et de colonnes du DataFrame
print("==== Type de chaque colonne ====")
print(df.dtypes) # Affiche le type de chaque colonne du DataFrame