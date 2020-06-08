import flask
from flask import Flask, jsonify, request
import json
from input_data import data_in
import numpy as np
import joblib

def load_models():
    file_name = "models/Gradient_Boost_reg.pkl"
    with open(file_name, 'rb') as gbr:
    model = joblib.load(file_name)
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])

def predict():
    # stub input features
    request_json = request.get_json()
    #x = request_json[data_in]
    model = load_models()
    prediction = model.predict(data_in)
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)