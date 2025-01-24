from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Conexión a MongoDB
client = MongoClient("mongodb+srv://emarcasdev:Lgv5EiO0N1RAxRiX@emarcasdev.hlq6d.mongodb.net/?retryWrites=true&w=majority&appName=emarcasdev") 
db = client["express_back"]
users_collection = db["users"]

# Prueba anterior
# users = [
#     {"id": 1, "nombre": "Eder", "apellido": "Martínez", "tlfn": 657543209},
#     {"id": 2, "nombre": "David", "apellido": "Puga", "tlfn": 657543209},
#     {"id": 3, "nombre": "Diego", "apellido": "Perez", "tlfn": 657543209},
#     {"id": 4, "nombre": "Agus", "apellido": "Alonso", "tlfn": 657543209}
# ]

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/about')
def about():
    return 'About'

@app.route('/api/users', methods=["GET"])
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))
    return jsonify(users)

@app.route('/api/users', methods=["POST"])
def add_user():
    # Recuperamos los datos necesarios del front
    data = request.get_json()
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    telefono = data.get("telefono")

    try:
        # Contamos la cantidad de documentos existentes en la colección
        user_count = users_collection.count_documents({},)
        # Creamos el nuevo usuario con el id incrementado
        new_user = {
            "id": user_count + 1,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono
        }
        # Insertamos el nuevo usuario en la colección
        result = users_collection.insert_one(new_user)
        # Devolvemos el ID del nuevo documento insertado
        return jsonify({"insertedId": str(result.inserted_id)}), 201
    except Exception as e:
        print("Error al agregar el usuario:", e)
        return jsonify({"error": "Error al agregar el usuario"}), 500

@app.route('/api/user1', methods=["GET"])
def get_user_one():
    user = users_collection.find_one({"id": 1}, {"_id": 0})

    if user:
        return jsonify(user)  
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/api/user', methods=["GET"])
def get_user_by_id():
    user_id = request.args.get("id", type=int)
    user = users_collection.find_one({"id": user_id}, {"_id": 0})

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


app.run()