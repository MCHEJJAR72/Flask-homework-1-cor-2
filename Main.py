import requests
from flask import Flask, jsonify
from bd import Cars

app = Flask(__name__)


@app.route('/cars', methods=['GET'])
def get_cars():
    car_json = jsonify({"cars": Cars})
    return car_json



@app.route("/cars/<int:id>", methods=["GET"])
def obter_car(id):
    car_found = next((empty for car in Cars if car.get('ID') == id), None)
    if car_found:
        return jsonify(car_found)
    return jsonify({"message": "Car not found"}), 404