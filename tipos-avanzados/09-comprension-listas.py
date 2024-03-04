usuarios = [
    ["Juan", 4],
    ["Pedro", 2], 
    ["Ana", 3],
    ["Maria", 1]
]

#nombres = []
#for usuario in usuarios:
#    nombres.append(usuario[0])
#print(nombres)

#transformacion de listas 
nombre = [usuario[0] for usuario in usuarios]
print(nombre) #resultado: ['Juan', 'Pedro', 'Ana', 'Maria']

# filtramos
nombres = [usuario for usuario in usuarios if usuario[1] >= 3]
print(nombres) #resultado: [['Juan', 4], ['Ana', 3]]

# con la comprension de listas podemos crear otras lista a partir de otra, filtrando, o modificando los elementos de la lista original.

#filtrar y modificar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)#resultado: ['Juan', 'Ana']

#map y filter son funciones que hacen lo mismo que las comprensiones de listas, pero son mas lentas.
nombres =list(map(lambda usuario: usuario[0], usuarios))
print(nombres)#resultado: ['Juan', 'Pedro', 'Ana', 'Maria']


# si evalua en True, devuelve el elemento , si evalua en False, no lo devuelve.
menos_usuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menos_usuarios)#resultado: [['Juan', 4], ['Ana', 3]]

