from collections import deque

fila = deque([1,2]) # Creamos una fila con dos elementos
fila.append(3) # Agregamos un elemento al final de la fila
fila.append(4) # Agregamos un elemento al final de la fila
fila.append(5) # Agregamos un elemento al final de la fila
print(fila) # Imprimimos la fila
fila.popleft() # Eliminamos el primer elemento de la fila
print(fila) # Imprimimos la fila
if not fila: # Verificamos si la fila esta vacia
    print("La fila esta vacia") # Imprimimos un mensaje


# Path: tipos-avanzados/15-pilas.py
pila = [1,2,3] # Creamos una pila con tres elementos
pila.append(4) # Agregamos un elemento al final de la pila
pila.append(5) # Agregamos un elemento al final de la pila
print(pila) # Imprimimos la pila
pila.pop() # Eliminamos el ultimo elemento de la pila
print(pila) # Imprimimos la pila
if not pila: # Verificamos si la pila esta vacia
    print("La pila esta vacia") # Imprimimos un mensaje
    
#lifo = last in first out (ultimo en entrar primero en salir).
# la pila solo usamos metodos append y pop.
