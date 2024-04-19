# Importez les bibliothèques nécessaires (pandas sous le nom pd). Chargez le fichier donnees_ventes.csv dans un DataFrame df.

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
print(df.describe())
