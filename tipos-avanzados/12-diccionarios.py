#aprendo diciconarios nombre valor 
#diccionario = {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python','Django','JavaScript']}

punto = {'x': 10, 'y': 20}
print(punto['x'])#imprime el valor de la llave x
punto['z'] = 20 #agrega una nueva llave con su valor

print(punto.get('z', 0))#obtiene el valor de la llave z, si no existe devuelve 0

#para eliminar una llave
del punto['x']
print(punto)

#para saber si una llave existe
print('z' in punto) #devuelve true o false

#iterar en un diccionario
for llave, valor in punto.items():
    print(llave, valor) #imprime las llaves y los valores
    
#uso de los valores de un diccionario
usuarios = [
    {'id': 1, 'nombre': 'Carlos'},
    {'id': 2, 'nombre': 'Cesar'},
    {'id': 3, 'nombre': 'Cristian'}
]

# acceder solo a los nombres de los usuarios
for usuario in usuarios:
    print(usuario['nombre']) #imprime solo los nombres de los usuarios

