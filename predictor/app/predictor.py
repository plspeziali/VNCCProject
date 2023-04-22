from flask import Flask, request, jsonify
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('model.pickle', 'rb') as f:
    model = pickle.load(f)

@app.route('/predictor', methods=['POST'])
def effettua_predizioni():
    # Riceve la richiesta POST contenente il JSON con i dati
    dati_json = request.get_json()

    # Converte il JSON in un DataFrame
    df = pd.DataFrame(dati_json, index=[0])

    df['height_m'] = df.height/100
    df['BMI'] = df.weight / df.height_m ** 2
    df.drop('height', axis=1, inplace=True)
    df.drop('height_m', axis=1, inplace=True)
    df.drop('weight', axis=1, inplace=True)

    # sex = df[['gender']]
    # oneHot = OneHotEncoder(sparse=False)
    # sex = pd.DataFrame(oneHot.fit_transform(sex), columns=oneHot.get_feature_names_out())
    # df.drop(columns=['gender'], axis=1, inplace=True)
    # df = pd.concat([sex, df], axis=1)
    # df = df.rename(columns={'x0_F': 'F'})
    # df = df.rename(columns={'x0_M': 'M'})

    # return df.head().to_json()

    # Standardization
    # sc = StandardScaler()
    # df = sc.fit_transform(df)

    # Esegue la predizione sui dati utilizzando il modello
    risultato = model.predict(df)

    # Restituisce il risultato della predizione in formato JSON
    return jsonify(risultato.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
