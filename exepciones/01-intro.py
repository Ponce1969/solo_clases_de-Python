# Aprendemos de las Excepciones
# Las excepciones son errores que ocurren durante la ejecución del programa.
# Las excepciones son objetos que se crean cuando ocurre un error y contienen información sobre el error.
# Si no se manejan, las excepciones causan que el programa termine.
# usamos try y except para manejar excepciones.
try:
    n1 = int(input("Ingrese un numero: "))# en vez de pasar un numero, pasamos un string y esto genera un error de tipo ValueError

except:
    print("No ingresaste un numero")#si no se maneja la excepcion, el programa termina y no se ejecuta el print de abajo.   
    
