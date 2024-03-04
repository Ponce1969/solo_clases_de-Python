# calculadora interactiva, verificar que el usuario ingrese un número y luego ingrese la operacion a realizar
# mostrar resultados y preguntar si desea continuar
#el resultado se guarda como el primer numero, y el usuario ingrese la segunda operacion
#las operaciones son suma, multi, div y resta.
#ingresaoperacion a realizar y cuando quiera poner salir, que termine el programa.


# solucion
print("Bienvenido a la calculadora interactiva")
print("Para salir escriba salir")
print("Las operaciones disponibles son: suma, resta, multi, div")

resultado = " "

while True:
    resultado = input("Digite primer numero:  ")
    if resultado.lower() == "salir":
            break
    resultado = int(resultado)
    operacion = input("Digite operacion a realizar: ")
    if operacion == "salir":
        break
    n2 = input("Digite segundo numero: ")
    if n2.lower() == "salir":
         break 
    n2 = int(n2)
    if operacion.lower() == "suma":
        resultado += n2
    elif operacion.lower() == "resta":
        resultado -= n2
    elif operacion.lower() == "multi":
        resultado *= n2
    elif operacion.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break
    print(f"El resultado es: {resultado}")  
        

 
