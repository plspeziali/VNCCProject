from flask import Flask, request
import psycopg2
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
def inserisci_dati():
    age = request.json['age']
    gender = request.json['gender']
    height = request.json['height']
    weight = request.json['weight']
    body_fat = request.json['body_fat']
    diastolic = request.json['diastolic']
    systolic = request.json['systolic']
    bend_forward = request.json['bend_forward']
    grip_force = request.json['grip_force']
    sit_ups = request.json['sit_ups']
    broad_jump = request.json['broad_jump']
    class_value = request.json['class_value']

    conn = psycopg2.connect(database="body-performance", host="db", user="admin", password="admin", port="5432")
    cur = conn.cursor()

    query = "INSERT INTO body_performance (age, gender, height, weight, body_fat, diastolic, systolic, bend_forward, grip_force, sit_ups, broad_jump, class) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (age, gender, height, weight, body_fat, diastolic, systolic, bend_forward, grip_force, sit_ups, broad_jump, class_value)
    cur.execute(query, data)

    cur.close()
    conn.commit()
    conn.close()

    
    response = requests.get('http://localhost:3002/train')
    print(response.text)


    return "Dati inseriti con successo nel database!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)