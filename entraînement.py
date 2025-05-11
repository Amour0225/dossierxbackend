# entrainement.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Charger le fichier CSV
df = pd.read_csv('data/match_data_example.csv')  # Assure-toi que le fichier est dans un dossier /data

# Encodage des variables catégorielles
df = pd.get_dummies(df, columns=['equipe_domicile', 'equipe_exterieure', 'forme_domicile', 'forme_exterieure'])

# Séparation des variables
X = df.drop(columns=['fautes', 'cartons', 'buts', 'possession'])
y_fautes = df['fautes']
y_cartons = df['cartons']
y_buts = df['buts']
y_possession = df['possession']

# Séparer les données (80% entraînement, 20% test)
X_train, X_test, y_fautes_train, y_fautes_test = train_test_split(X, y_fautes, test_size=0.2, random_state=42)
_, _, y_cartons_train, y_cartons_test = train_test_split(X, y_cartons, test_size=0.2, random_state=42)
_, _, y_buts_train, y_buts_test = train_test_split(X, y_buts, test_size=0.2, random_state=42)
_, _, y_possession_train, y_possession_test = train_test_split(X, y_possession, test_size=0.2, random_state=42)

# Normalisation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modèle Random Forest pour chaque cible
def train_and_evaluate_model(y_train, y_test, label):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"{label} - MSE: {mse:.2f}, R2: {r2:.2f}")
    return model

# Entraînement et évaluation
train_and_evaluate_model(y_fautes_train, y_fautes_test, "Fautes")
train_and_evaluate_model(y_cartons_train, y_cartons_test, "Cartons")
train_and_evaluate_model(y_buts_train, y_buts_test, "Buts")
train_and_evaluate_model(y_possession_train, y_possession_test, "Possession")