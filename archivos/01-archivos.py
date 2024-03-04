from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt") # Crear un objeto de tipo Path
#archivo.exists() # True
#archivo.rename()
#archivo.unlink() # Elimina el archivo

#print(archivo.stat()) # Información del archivo

#print("acceso ", archivo.stat().st_atime) # Fecha de último acceso timestamp fecha unix

print("acceso", ctime(archivo.stat().st_atime)) # Fecha de último acceso  Thu Feb  8 22:56:34 2024
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
