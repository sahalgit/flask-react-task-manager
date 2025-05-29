from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
import psycopg2
import time

app = Flask(__name__)
CORS(app)

# Retry DB connection
for _ in range(5):
    try:
        conn = psycopg2.connect(
            host="db",
            database="flaskdb",
            user="flaskuser",
            password="flaskpass"
        )
        conn.autocommit = True
        break
    except psycopg2.OperationalError:
        print("Postgres not ready, retrying in 2 seconds...")
        time.sleep(5)
else:
    raise Exception("Could not connect to the database after 5 tries")

cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL
    );
""")

# GET home page (optional if using API only)
@app.route("/")
def index():
    return "Flask + Postgres API is running."

# GET all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    cur.execute("SELECT id, title FROM tasks;")
    tasks = [{"id": row[0], "title": row[1]} for row in cur.fetchall()]
    return jsonify(tasks)

# POST new task
@app.route("/tasks", methods=["POST"])
def add_task():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    print("Incoming JSON:", data)

    task = data.get("task")
    if not task or not task.strip():
        return jsonify({"error": "Task title required"}), 400

    cur.execute("INSERT INTO tasks (title) VALUES (%s) RETURNING id;", (task,))
    task_id = cur.fetchone()[0]
    conn.commit()
    return jsonify({"id": task_id, "title": task}), 201

# DELETE task by ID
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id;", (task_id,))
    deleted = cur.fetchone()
    conn.commit()
    if deleted:
        return jsonify({"message": f"Task {task_id} deleted"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
