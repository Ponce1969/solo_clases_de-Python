#Aprendo a extender tipos nativos.
#En este caso, extenderemos el tipo nativo list.

lista =  list([1,2,3])
lista.append(4)
# Si quiero agregar al principio de la lista, debo usar insert
lista.insert(0,0)
print(lista)


#si bien esto funciona hay una forma mas elegante de hacerlo y es extender el tipo nativo list
#para eso debemos crear una clase que herede de list
#y luego sobreescribir el metodo append
#y luego instanciar la clase
#luego llamar al metodo prepend


class ListaMejorada(list):#hereda de list
    def prepend(self, valor):
        self.insert(0, valor)
        
lista = ListaMejorada([1,2,3])
lista.append(4)
lista.prepend(0)#llamamos al metodo prepend que creamos en la clase ListaMejorada que hereda de list.
print(lista)