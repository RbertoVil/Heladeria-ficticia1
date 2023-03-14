from flask import Flask, render_template, request, redirect, url_for
import databaseConfig

app = Flask(__name__)

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

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    return render_template("login.html", error = error)

@app.route("/insertar", methods=["GET", "POST"])
def insertarDatos():
    if request.method == "POST":
        # Seleccionamos los datos a ingresar
        name = request.form["add-name"]
        description = request.form["add-description"]
        price = request.form["add-price"]

        # Insertamos los datos:
        databaseConfig.insertar(name, description, price)

    return render_template("insertarDatos.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Si intentan ingresar a /admin de forma incorrecta
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "r1234":
            # credenciales incorrectas
            error = " Credenciales incorrectas."
            return render_template("login.html", error = error)
    elif request.method == "GET":
        # Si intentan ingresar a /admin de forma directa
        return render_template("login.html")

# Para eliminar y editar datos usar el "i"
#for i in cursor:
#    print(i)

    conexionDB = databaseConfig.conectar("prueba3")
    conexion = conexionDB[0]
    cursor = conexionDB[1]

    lineas = []
    cursor.execute("SELECT * FROM menu;")
    for i in cursor:
        lineas.append(i)

    conexion.close()

    return render_template("admin.html", lineas = lineas)
