from flask import Flask, render_template, request, redirect, url_for
import os
import databaseConfig

# IMG_FOLDER = "/static/img" # Es más simple, pero solo sirve para sistemas operativos POSIX
# Porque estos usan el separador del path slash ('/')
IMG_FOLDER = os.path.join('static', 'img') # implementación multiplataforma
# Porque utiliza el separador del path correspondiente al SO

app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER
# print(app.config) # For debbuging

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

@app.route("/editar", methods=["GET", "POST"])
def editarDatos():
    if request.method == "POST":
        # Seleccionamos los datos a ingresar/eliminar
        ID = request.form["edit-id"]
        name = request.form["edit-name"]
        description = request.form["edit-description"]
        price = request.form["edit-price"]
        mode = request.form["edit-mode"]

        # Datos previos (para compararlos)
        oldName = request.form["old-name"]
        oldDescription = request.form["old-description"]
        oldPrice = request.form["old-price"]

        if mode == "editar":
            # Editamos los datos:
            print("editando los datos...")
            if name != oldName:
                print("Editando Name")
                databaseConfig.editar(ID, "name", name, "str")
            if description != oldDescription:
                print("Editando description")
                databaseConfig.editar(ID, "description", description, "str")
            if price != oldPrice:
                print("Editando price")
                databaseConfig.editar(ID, "price", price, "float")

        # Eliminamos los datos:

    return render_template("editarDatos.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Las direcciones de las imagenes:
    imgEdit = os.path.join(app.config['IMG_FOLDER'], "editar.svg")
    imgDelete = os.path.join(app.config['IMG_FOLDER'], "cruz.svg")

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

    return render_template("admin.html", lineas = lineas, imgEdit = imgEdit, imgDelete = imgDelete)
