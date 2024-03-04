from io import open


# solo para escritura

texto = "Hola mundo!"

#archivo = open("archivos/hola-mundo.txt", "w") # Crear un archivo
#archivo.write(texto) # Escribir en el archivo
#archivo.close() # Cerrar el archivo muy importante para que se guarde el contenido en el archivo

# solo para lectura

#archivo = open("archivos/hola-mundo.txt", "r") # Abrir un archivo
#texto = archivo.read() # Leer el contenido del archivo
#archivo.close() # Cerrar el archivo
#print(texto) # Hola mundo!

#lectura como lista

#archivo = open("archivos/hola-mundo.txt", "r") # Abrir un archivo
#texto = archivo.readlines() # Leer el contenido del archivo
#archivo.close() # Cerrar el archivo
#print(texto) # ['Hola mundo!']

# cerramos archivos con with y metodos magicos de __enter__ y __exit__ que cierran el archivo
# with y seek para regresar el cursor al inicio del archivo
#with open("archivos/hola-mundo.txt", "r") as archivo: # Abrir un archivo
    # print(archivo.readlines()) # Leer el contenido del archivo
    # archivo.seek(0) # Regresar el cursor al inicio del archivo
    # for linea in archivo:
        # print(linea)
         
 
 # Agregar texto al archivo
#with open("archivos/hola-mundo.txt", "a+") as archivo: # Abrir un archivo
 #   archivo.write("Adios mundo!") # Escribir en el archivo
  #  archivo.close() # Cerrar el archivo
    

# lectura y escritura
with open("archivos/hola-mundo.txt", "r+") as archivo: # Abrir un archivo
    texto = archivo.readlines() # Leer el contenido del archivo
    archivo.seek(0) # Regresar el cursor al inicio del archivo
    texto[0] = "Chanchito feliz la" 
    archivo.writelines( texto) # Escribir en el archivo
       