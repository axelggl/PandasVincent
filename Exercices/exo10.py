# Utilisez matplotlib ou seaborn pour visualiser les tendances des revenus au cours du temps.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('donnees_ventes.csv')
df['Date'] = pd.to_datetime(df['Date']) # Convertit la colonne Date en datetime
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire'] # Crée une nouvelle colonne Revenu en multipliant les colonnes Quantité vendue et Prix unitaire
df['Année'] = pd.to_datetime(df['Date']).dt.year # Crée une nouvelle colonne Année en extrayant l'année de la colonne Date

df.groupby('Année')['Revenu'].sum().plot(kind='line', title='Revenus au cours du temps')
plt.ylabel('Revenu total')
plt.show() # Affiche le graphique des tendances des revenus au cours du temps