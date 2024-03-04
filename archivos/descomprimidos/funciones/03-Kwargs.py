#kwargs argumentos con nombre clave.
def get_user(**datos): # **kwargs parametros infinitos con ** se le dice a python que va a recibir una cantidad infinita de argumentos.
    print(datos)
    print(type(datos))
    print(datos['nombre']) #accedemos a los valores de los argumentos con nombre clave diccionario.
    print(datos['apellido'])
    print(datos['edad'])
    print(datos['email'])
    print(datos['telefono'])
    print(datos['direccion'])
    print(datos['ciudad'])
    print(datos['pais'])
    
    
    
def get_product(**datos):
    print(datos["id"], datos["name"] )
    
    
get_product(id ="23" ,
            name = "iphone",
            desc="Esto es un iphone " )


