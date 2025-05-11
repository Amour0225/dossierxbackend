import os
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

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
    data = request.get_json()

    # Données reçues (à adapter selon ton frontend)
    var_input = data.get('var_input')
    corners_input = data.get('corners_input')
    buts_input = data.get('buts_input')
    fautes_input = data.get('fautes_input')
    cartons_input = data.get('cartons_input')
    possession_input = data.get('possession_input')

    # Prédictions simulées (remplacer par tes vrais modèles ensuite)
    var_prediction = 'VAR probable' if var_input else 'VAR improbable'
    corners_prediction = 'Plus de 10 corners' if corners_input else 'Moins de 10 corners'
    buts_prediction = f"{buts_input} buts probables" if buts_input is not None else "Buts inconnus"
    fautes_prediction = f"{fautes_input} fautes probables" if fautes_input is not None else "Fautes inconnues"
    cartons_prediction = f"{cartons_input} cartons probables" if cartons_input is not None else "Cartons inconnus"
    possession_prediction = f"{possession_input}% de possession attendue" if possession_input is not None else "Possession inconnue"

    return jsonify({
        'var_prediction': var_prediction,
        'corners_prediction': corners_prediction,
        'buts_prediction': buts_prediction,
        'fautes_prediction': fautes_prediction,
        'cartons_prediction': cartons_prediction,
        'possession_prediction': possession_prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
