# invocamos la excepcion
# raise NameError("Hemos invocado la excepcion")
def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 5/n


try:
     division()
except ZeroDivisionError as e:# ZeroDivisionError es una clase hija de Exception, por eso se puede usar para manejar solo excepciones de tipo ZeroDivisionError.
    print(e)
    
    
