# loops anidados ejemplo;

for j in range(3):# j es un numero entero (outer loop)
    for k in range(2):# k es un numero entero(inner loop)
        print(f" {j},  {k}")
        
        
# pensar mucho en usar for loops anidados, ya que pueden ser muy complejos.
# el resultado de este for anidado es:
#  0,  0  J=0, K=0
#  0,  1  J=0, K=1 # en este punto itera sobre k, y luego vuelve a iterar sobre j
#  1,  0  J=1, K=0
#  1,  1  J=1, K=1
#  2,  0  J=2, K=0
#  2,  1  J=2, K=1


        