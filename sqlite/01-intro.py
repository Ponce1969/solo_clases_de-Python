import sqlite3

# Create a connection to the database
con = sqlite3.connect('sqlite/app.db') # si la base de datos no existe, se crea
con.close()  # Cerrar la conexión con la base de datos (siempre se debe cerrar la conexión)


