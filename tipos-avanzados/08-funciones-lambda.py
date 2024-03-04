# ejemplos de funciones lambda, o anonimas.
usuarios = [
    ["Juan", 4],
    ["Pedro", 2], 
    ["Ana", 3],
    ["Maria", 1]
    
]   #nos ahorramos de escribir la funcion ordena, y la funcion lambda es mas rapida.

usuarios.sort(key= lambda elemento: elemento[1])#ordena la lista de menor a mayor por el primer elemento de cada lista
print(usuarios)

