from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
    {"id": 1, "nombre": "Eder", "apellido": "Martínez", "tlfn": 657543209},
    {"id": 2, "nombre": "David", "apellido": "Puga", "tlfn": 657543209},
    {"id": 3, "nombre": "Diego", "apellido": "Perez", "tlfn": 657543209},
    {"id": 4, "nombre": "Agus", "apellido": "Alonso", "tlfn": 657543209}
]

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/about')
def about():
    return 'About'

@app.route('/api/users', methods=["GET"])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=["POST"])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/user1', methods=["GET"])
def get_user_one():
    user_id = 1  
    user = next((user for user in users if user["id"] == user_id), False)

    if user:
        return jsonify(user)  
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/api/user', methods=["GET"])
def get_user_by_id():
    user_id = request.args.get("id", type=int)
    user = next((user for user in users if user["id"] == user_id), False)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


app.run()