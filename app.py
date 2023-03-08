from flask import Flask, render_template, request
import databaseConfig

app = Flask(__name__)

conexionDB = databaseConfig.conectar("prueba")
conexion = conexionDB[0]
cursor = conexionDB[1]

cursor.execute("SELECT * FROM tabla1;")
for i in cursor:
    print(i)

conexion.close()

@app.route("/")
def heladeria():
    return render_template("index.html")
