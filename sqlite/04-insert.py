import sqlite3

# Datos a insertar
usuario = (1, "Hola Mundo")

# Se crea la conexión a la base de datos
with sqlite3.connect('sqlite/app.db') as con:
    cursor = con.cursor()  # Se crea un cursor para ejecutar sentencias SQL

    # Se crea la tabla "usuarios" si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT
    );
    """)

    # Se ejecuta la consulta de inserción con parámetros de marcadores de posición
    cursor.execute("INSERT INTO usuarios VALUES (?, ?);", usuario)


    