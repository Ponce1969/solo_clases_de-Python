from pathlib import Path

# trabajar con archivos de lectura y escritura , la mejor manera de trabajar con archivos

archivo = Path("archivos/archivo-prueba.txt") # Crear un objeto de tipo Path
texto = archivo.read_text("utf-8").split("\n")   # Leer el contenido del archivo
texto.insert(0, "Hola mundo") # Agregar una línea al archivo
archivo.write_text("\n".join(texto), "utf-8" ) # Escribir en el archivo

