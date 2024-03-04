from pathlib import Path
from zipfile import ZipFile

# trabajamos con with para que se cierre el archivo
with ZipFile("archivos/comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)