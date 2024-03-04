# and, or, not

# and   -> y    -> True si ambos son True
# or    -> o    -> True si alguno es True
# not   -> no   -> True si es False, False si es True es una negacion.


# Ejemplo 1 
gas = True
encendido = True
if gas and encendido:
    print("puedes avanzar")
else:
    print("no puedes avanzar")
    
    
    
# Ejemplo 2
gas = False
encendido = True
if gas or encendido:
    print("puedes avanzar")
else:
    print("no puedes avanzar")
    

# Ejemplo 3
gas = False
encendido = True
edad = 18  # en este caso la edad es mayor a 17, pero no se puede avanzar porque el carro no tiene gasolina.
if  gas and (encendido or edad > 17):# parentesis para darle prioridad a la edad.
    print("puedes avanzar")
    
    
# Ejemplo 4
gas = False
encendido = True
edad = 18 
if not gas and (encendido or edad > 17): # not es una negacion, en este caso es False, pero como esta negado es True.
    print("puedes avanzar")# puede avanzar porque el carro tiene gasolina por la negacion de not.
       

# operadores de corto circuito
# and -> si el primero es False, no evalua el segundo.
# or -> si el primero es True, no evalua el segundo.

# Ejemplo 5
gas = False
encendido = True
edad = 18

if not gas and encendido and edad > 17:# si el primero es False, no evalua el segundo.
    print("puedes avanzar") #se ejecuta de izquierda a derecha,ahorra tiempo de ejecucion y mejora el rendimiento.
    
# Ejemplo 6
gas = True
encendido = True
edad = 18
                                       #si el valor de la izquierda es Falso si evalua el segundo.
if  not gas or encendido or edad > 17:# por lo menos uno tiene que ser True, y todo evalua True, no evalua el segundo.
    print("puedes avanzar") #se ejecuta de izquierda a derecha,ahorra tiempo de ejecucion y mejora el rendimiento.
