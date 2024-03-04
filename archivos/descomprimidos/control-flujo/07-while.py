# aprendemos a usar el bucle while
#numero = 1
#while numero < 100:
#   print(numero)
#   numero *= 2
    
# el bucle while se ejecuta mientras la condicion sea verdadera

comando = ""
while comando.lower() != "salir": # lower() convierte el texto a minusculas
    comando = input("$ ")
    print(comando)
    

#ejemplo de loops infinitos
#while True:
#    comando = input("$ ")
#    print(comando)
#    if comando.lower() == "salir":
#        break # break rompe el loop
#    print("saliendo...")
# importante no olvidar el break para que no se ejecute infinitamente

