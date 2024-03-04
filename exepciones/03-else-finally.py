#Aprendemos de las Excepciones
#else y finally

try:
    n1 = int(input("Ingrese un numero: "))
    
except Exception as e:
    print("No ingresaste un numero")
    
else:# se ejecuta si no se produce ninguna excepcion
    print("Todo salio bien")
    
finally:# se ejecuta siempre, haya o no excepcion
    print("Fin del programa")
    
# si no se produce ninguna excepcion, se ejecuta el bloque else y luego el finally
