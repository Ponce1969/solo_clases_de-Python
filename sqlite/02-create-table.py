import sqlite3

# crear tablas en la base de datos

con = sqlite3.connect('sqlite/app.db')
cur = con.cursor()# Crear un cursor para ejecutar sentencias SQL
con.execute(   # Ejecutar una sentencia SQL
    """
    CREATE TABLE IF NOT EXISTS users 
    (id INTEGER prymari key, nombre VARCHAR(50));   # Crear una tabla llamada users con dos columnas: id y nombre
    """   
)
con.commit() # Confirmar los cambios en la base de datos
con.close()  # Cerrar la conexión con la base de datos (siempre se debe cerrar la conexión)