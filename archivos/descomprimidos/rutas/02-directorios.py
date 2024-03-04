from pathlib import Path

path = Path("rutas")
#path.mkdir() # crea el directorio
#path.rmdir() # elimina el directorio
#path.exists() # False
#path.rename("chanchito feliz") # renombra el directorio

#print(path.iterdir()) # <generator object Path.iterdir at 0x7f3e3e3e3f90>


#for p in path.iterdir():
#    print(p)   # rutas/01-archivos.py

#archivos = [p for p in path.iterdir() if not p.is_dir()]
#print(archivos) # [PosixPath('rutas/01-archivos.py'), PosixPath('rutas/02-directorios.py')]

#archivos = [p for p in path.rglob("*.py")]
#print(archivos) # [PosixPath('rutas/01-archivos.py'), PosixPath('rutas/02-directorios.py')]

