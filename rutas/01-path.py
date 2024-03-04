from pathlib import Path

# Crear un objeto Path
#Path("/usr/bin") # ruta absoluta
#Path("one/__init__.py") # ruta relativa


path = Path("hola-mundo/mi-archivo.py")
path.is_file() # True
path.is_dir() # False
path.exists() # True

print(
    path.name, # mi-archivo.py
    path.stem, # mi-archivo
    path.suffix, # .py
    path.parent, # hola-mundo
    path.absolute(), # /home/usuario/hola-mundo/mi-archivo.py   
)

p = path.with_name("chanchito.py")
print(p) # hola-mundo/chanchito.py

p = path.with_suffix(".bat")
print(p) # hola-mundo/mi-archivo.bat

p = path.with_stem("feliz")
print(p) # hola-mundo/feliz.py


