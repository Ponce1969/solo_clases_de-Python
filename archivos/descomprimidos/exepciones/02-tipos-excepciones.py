try: 
    n1 = int(input("Ingrese un numero: "))

except Exception as e:# Exception es la clase padre de todas las excepciones, por eso se puede usar para manejar cualquier tipo de excepcion.
    print("No ingresaste un numero")
    


#try: 
#    n1 = int(input("Ingrese un numero: "))
    
#except ValueError as e:# ValueError es una clase hija de Exception, por eso se puede usar para manejar solo excepciones de tipo ValueError.
 #   print("No ingresaste un numero")
 
 
#try:
#    n1 = int(input("Ingrese un numero: "))

#except NameError as e:# NameError es una clase hija de Exception, por eso se puede usar para manejar solo excepciones de tipo NameError.
#    print("No ingresaste un numero")

# con esto fallamos elegante y podemos seguir ejecutando el programa.