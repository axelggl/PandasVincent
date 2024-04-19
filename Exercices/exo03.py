# Vérifiez et traitez les valeurs manquantes. Supprimez les éventuelles lignes dupliquées.

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
print("==== Valeurs manquantes ====")
print(df.isnull().sum()) # Affiche le nombre de valeurs manquantes par colonne
print("==== Lignes dupliquées ====")
print(df.duplicated().sum()) # Affiche le nombre de lignes dupliquées
print("==== Suppression des lignes dupliquées ====")
df.drop_duplicates(inplace=True) # Supprime les lignes dupliquées