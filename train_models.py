import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

# Remplace "matches.csv" par le chemin vers ton fichier CSV local
CSV_FILE = "matches.csv"

# Charger les données
df = pd.read_csv(CSV_FILE)

# Encodage des équipes
le_team1 = LabelEncoder()
le_team2 = LabelEncoder()
df["team1_encoded"] = le_team1.fit_transform(df["team1"])
df["team2_encoded"] = le_team2.fit_transform(df["team2"])

# Variables d'entrée
X = df[["team1_encoded", "team2_encoded"]]

# Exemple avec la cible 'fouls' (fautes)
y_fouls = df["fouls"]

# Entraîner un modèle RandomForestRegressor pour prédire les fautes
model_fouls = RandomForestRegressor()
model_fouls.fit(X, y_fouls)

# Sauvegarder le modèle et les encodeurs
with open("model_fouls.pkl", "wb") as f:
    pickle.dump(model_fouls, f)
with open("le_team1.pkl", "wb") as f:
    pickle.dump(le_team1, f)
with open("le_team2.pkl", "wb") as f:
    pickle.dump(le_team2, f)

print("Modèle et encodeurs enregistrés avec succès.")