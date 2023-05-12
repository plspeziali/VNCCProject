from flask import Flask, render_template, request
import requests
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    response = requests.post('http://predictor:5000', json=data)
    return response.text

@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    response = requests.post('http://inserter:3001', json=data)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
