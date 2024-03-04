#mostramos el uso del depurador.

def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado# aqui se puede dar el error de identacion.


print("Chanchito")
l = largo("Hola mundo")
print(l)

#para depurar el codigo se usa el comando python -m pdb nombre.py
#para salir del depurador se usa el comando q
#para ver la linea actual se usa el comando l
#para avanzar a la siguiente linea se usa el comando n
#para ver el valor de una variable se usa el comando p nombre_variable
#para avanzar a la siguiente linea se usa el comando n
# para mas info se puede usar el comando h
#https://code.visualstudio.com/docs/editor/debugging#_launch-configurations

