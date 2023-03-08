from flask import Flask, render_template, request
import databaseConfig

app = Flask(__name__)

#cursor.execute("SELECT * FROM menu;")
#for i in cursor:
#    print(i)

@app.route("/")
def heladeria():
    return render_template("index.html")

@app.route("/menu")
def menu():
    conexionDB = databaseConfig.conectar("prueba3")
    conexion = conexionDB[0]
    cursor = conexionDB[1]

    lineas = []
    cursor.execute("SELECT * FROM menu;")
    for i in cursor:
        lineas.append(i)

    conexion.close()

    return render_template("menu.html", lineas = lineas)
