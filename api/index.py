from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Eder"},
    {"id": 2, "name": "David"},
    {"id": 3, "name": "Diego"},
    {"id": 4, "name": "Agus"}
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

@app.route('/api/users1', methods=["GET"])
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