#manipular listas
mascotas = ['perro','gato','pez','conejo','pulga']
print(mascotas[0])#imprime perro
print(mascotas[1])#imprime gato
print(mascotas[2])#imprime pez

mascotas[0] = 'Bicho'
print(mascotas[0])#imprime Bicho

#obtener parte parcial de la lista
print(mascotas[0:2])#imprime ['Bicho','gato']
print(mascotas[1:3])#imprime ['gato','pez']
print(mascotas[-1])#imprime pulga
print(mascotas[ : :2])#imprime ['Bicho','pez','pulga']

numeros = list(range(21))
print(numeros[1: :2])#imprime [1,3,5,7,9,11,13,15,17,19] numeros impares.
print(numeros[ : :2])#imprime [0,2,4,6,8,10,12,14,16,18,20] numeros pares.
