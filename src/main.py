from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL DB connection function
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='crud'
    )

# # Get all users
# @app.route('/api/users', methods=['GET'])
# def get_users():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return jsonify(users)

# # Get a single user
# @app.route('/api/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     user = cursor.fetchone()
#     cursor.close()
#     conn.close()
#     if user:
#         return jsonify(user)
#     return jsonify({"error": "User not found"}), 404

# # Create a new user
# @app.route('/api/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     age = data.get('age')

#     if not name or not email or not age:
#         return jsonify({"error": "Missing fields"}), 400

#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
#     conn.commit()
#     user_id = cursor.lastrowid
#     cursor.close()
#     conn.close()

#     return jsonify({"id": user_id, "name": name, "email": email, "age": age}), 201

# # Update a user
# @app.route('/api/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     age = data.get('age')

#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s", (name, email, age, user_id))
#     conn.commit()
#     affected_rows = cursor.rowcount
#     cursor.close()
#     conn.close()

#     if affected_rows == 0:
#         return jsonify({"error": "User not found"}), 404

#     return jsonify({"message": "User updated successfully"})

# # Delete a user
# @app.route('/api/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
#     conn.commit()
#     affected_rows = cursor.rowcount
#     cursor.close()
#     conn.close()

#     if affected_rows == 0:
#         return jsonify({"error": "User not found"}), 404

#     return jsonify({"message": "User deleted successfully"})

# Run the API
if __name__ == '__main__':
    app.run(debug=True)
