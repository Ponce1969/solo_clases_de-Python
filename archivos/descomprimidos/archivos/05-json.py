import json
from pathlib import Path


# escribir un archivo json----
#productos = [
 #   {"id": 1, "name": "Surfboard"},
  #  {"id": 2, "name": "Bicicleta"},
   # {"id": 3, "name": "Skate"},
    
#]


#data = json.dumps(productos)
#Path("archivos/productos.json").write_text(data)

# leer un archivo json----
data = Path("archivos/productos.json").read_text()
productos = json.loads(data)
#print(productos)

# modificar un archivo json----
productos[0]["name"] = "Chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))


