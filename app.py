import os
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Vérification du fichier CSV
CSV_FILE = "dossierx_match_data.csv"
if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"Erreur : Le fichier '{CSV_FILE}' est introuvable.")
else:
    print("Fichier trouvé, chargement en cours...")

@app.route('/')
def home():
    return 'Dossier X Backend API is running'

@app.route('/api/match-predictions', methods=['GET'])
def match_predictions():
    try:
        df = pd.read_csv(CSV_FILE)
        return jsonify(df.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        team1 = data.get('team1')
        team2 = data.get('team2')

        # Charger les fichiers nécessaires
        with open("model_fouls.pkl", "rb") as f:
            model_fouls = pickle.load(f)
        with open("le_team1.pkl", "rb") as f:
            le_team1 = pickle.load(f)
        with open("le_team2.pkl", "rb") as f:
            le_team2 = pickle.load(f)

        # Encoder les noms d'équipes
        team1_encoded = le_team1.transform([team1])[0]
        team2_encoded = le_team2.transform([team2])[0]

        # Faire une prédiction
        X = [[team1_encoded, team2_encoded]]
        predicted_fouls = model_fouls.predict(X)[0]

        return jsonify({
            "team1": team1,
            "team2": team2,
            "predicted_fouls": round(predicted_fouls)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)