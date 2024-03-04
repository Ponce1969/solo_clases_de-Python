import sqlite3

# crear tablas en la base de datos con with

with  sqlite3.connect('sqlite/app.db') as con: # Crear una conexión a la base de datos
   cursor = con.cursor()# Crear un cursor para ejecutar sentencias SQL
   cursor.execute(   # Ejecutar una sentencia SQL
    """
    CREATE TABLE IF NOT EXISTS users 
    (id INTEGER prymari key, nombre VARCHAR(50));   # Crear una tabla llamada users con dos columnas: id y nombre
    """   
  ) 
