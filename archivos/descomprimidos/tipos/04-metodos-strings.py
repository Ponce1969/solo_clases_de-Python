animal = "chanCHito feliz" # string 
print(animal.upper()) # CHANCHITO FELIZ
print(animal.lower()) # chanchito feliz
print(animal.capitalize()) # Chanchito feliz
print(animal.title()) # Chanchito Feliz
print(animal.strip()) # quita los espacios al inicio y al final .lstrip() .rstrip() 
print(animal.replace("f", "g")) # reemplaza caracteres
print(animal.split(" ")) # convierte en lista

#encadenar los metodos de strings
print(animal.upper().strip().replace("F", "G")) # CHANCHITO GELIZ
print(animal.strip().capitalize())# primero strip, luego capitalize van de la mano.
print(animal.find("feliz")) # devuelve la posicion donde se encuentra la palabra.

# que ocurre si buscamos una cadena que no existe?
print(animal.find("Hola")) # devuelve -1 si no encuentra la palabra.
print("nCH" in animal) # devuelve True si encuentra la palabra.")
print("nCH" not in animal) # devuelve False si encuentra la palabra.")
