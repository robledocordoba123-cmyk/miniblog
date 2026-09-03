from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def hola():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "db"),
            user="postgres",
            password="secreto",
            dbname="postgres"
        )
        conn.close()
        return "Hola desde MiniBlog - conectado a la base de datos"
    except Exception as e:
        return f"Hola desde MiniBlog - error de conexión: {e}"

app.run(host="0.0.0.0", port=5000)

# rama feature/login