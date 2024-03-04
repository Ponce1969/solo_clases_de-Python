# palindromo
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
print(palindromo("Amor a roma"))


# otro ejemplo de palindromo    
def es_palindromo(texto):
    return palindromo(texto)
        
print("Abba", es_palindromo("Abba"))
print("Somos o no somos", es_palindromo("Somos o no somos"))
 
    
# eliminar espacios en blanco de una cadena de texto.
# tomar un texto y hacer reverse
# comparar el texto original con el texto invertido.
# si son iguales es un palindromo.
# si no son iguales no es un palindromo.
# retornar true o false.
def no_espace(texto):
    nuevo_texto = ""
    for letra in texto:
        if letra != " ":
            nuevo_texto += letra
    return nuevo_texto

def reverse(texto):
    texto_invertido = ""
    for letra in texto:
        texto_invertido = letra + texto_invertido
    return texto_invertido

def palindromo(texto):
    texto = no_espace(texto)
    texto_invertido = reverse(texto)
    return texto.lower() == texto_invertido.lower()
    
        
print(es_palindromo("amo la paloma")) # True
print(es_palindromo("Hola mundo"))# False
print(es_palindromo("Ana"))# True
print(es_palindromo("Somos o no somos"))# True
