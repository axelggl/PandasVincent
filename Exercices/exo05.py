# Sélectionnez les données des ventes qui ont eu lieu en 2022. Filtrez les données pour afficher uniquement les ventes où plus de 100 articles ont été vendus. 

import pandas as pd

df = pd.read_csv('donnees_ventes.csv')
df['Année'] = pd.to_datetime(df['Date']).dt.year # Crée une nouvelle colonne Année en extrayant l'année de la colonne Date
df_2022 = df[df['Année'] == 2022] # Sélectionne les données des ventes qui ont eu lieu en 2022
df_2022_plus_100 = df_2022[df_2022['Quantité vendue'] > 100] # Filtre les données pour afficher uniquement les ventes où plus de 100 articles ont été vendus
print(df_2022_plus_100) # Affiche les données filtrées