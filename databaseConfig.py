import mysql.connector

def conectar(nombreDataBase):
    try:
        # Intenta conectarse a la base de datos con el usuario admin
        conexion = mysql.connector.connect(
                host = "localhost",
                user = "admin",
                password = "r1234",
                database = nombreDataBase,
                )
        cursor = conexion.cursor()
    except mysql.connector.errors.ProgrammingError:
        # No se puede conectar a la base de datos.
        # O la base de datos no existe,
        # O el servidor de base de datos no esta activo.
        conexion = mysql.connector.connect(
                host = "localhost",
                user = "admin",
                password = "r1234",
                )

        # Creamos la base de datos y la usamos:
        cursor = conexion.cursor()
        cursor.execute(f"CREATE DATABASE { nombreDataBase };")
        cursor.execute(f"USE { nombreDataBase };")

    #try:
        # Creamos la tabla para almacenar los helados en venta:
        #cursor.execute("CREATE TABLE menu (id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(150), description VARCHAR(2000), price FLOAT);")
    #except:
        #pass

    return(conexion, cursor)

def insertar(addName, addDescription, addPrice):
    # Establecemos conexion con la base de datos para insertar filas
    conexionDB = conectar("prueba3")
    conexion = conexionDB[0]
    cursor = conexionDB[1]

    addName = "\'" + addName + "\'"
    addDescription = "\'" + addDescription + "\'"
    
    comando = f"INSERT INTO menu (name, description, price) VALUES ({ addName }, { addDescription }, { addPrice });"

    print("Ejecutando el comando:")
    print(comando)
    cursor.execute(comando)

    conexion.commit()

    print(cursor.rowcount, "Dato(s) insertado(s)")

    cursor.close()
    conexion.close()
    return(True)
