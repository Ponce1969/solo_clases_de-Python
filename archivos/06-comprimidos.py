from pathlib import Path
from zipfile import ZipFile

# trabajamos con with para que se cierre el archivo
#with ZipFile("archivos/comprimidos.zip", "w") as zip:
 #     if str(path) != "archivos/comprimidos.zip":
  #          zip.write(path)
  
  
with ZipFile("archivos/comprimidos.zip") as zip:
    #print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size,
    )
    zip.extractall("archivos/descomprimidos")