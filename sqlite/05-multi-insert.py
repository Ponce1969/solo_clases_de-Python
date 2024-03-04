import sqlite3

# Datos de los usuarios a insertar
usuarios = [
    (2, "Chanchito feliz"),
    (3, "Chanchito triste")
]

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

    # Se ejecuta la consulta de inserción con parámetros de marcadores de posición para cada usuario
    for usuario in usuarios:
        cursor.executemany("INSERT INTO usuarios VALUES (?, ?);", usuario)


# este codigo de aca abajo es porque si ejecutamos dos veces el script, nos dara error ya que la tabla ya existe y no se puede volver a crear
# para solucionar esto, se puede borrar la tabla y volver a crearla como este codigo de abajo.
import sqlite3

# Datos de los usuarios a insertar
usuarios = [
    (2, "Chanchito feliz"),
    (3, "Chanchito triste")
]

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

    # Se eliminan las filas existentes con los mismos IDs
    for usuario in usuarios:
        cursor.execute("DELETE FROM usuarios WHERE id = ?;", (usuario[0],))

    # Se ejecuta la consulta de inserción con parámetros de marcadores de posición para cada usuario
    for usuario in usuarios:
        cursor.executemany("INSERT INTO usuarios VALUES (?, ?);", usuario)








