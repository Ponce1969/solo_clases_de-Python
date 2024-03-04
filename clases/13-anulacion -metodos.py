# anulando metodos
class Ave:
    def vuela(self):
        print('Vuela ave')
        
        
class Pato(Ave):
    def vuela(self):
        super().vuela()# aqui se ejecuta el metodo de la clase Ave, con super( ) se llama al metodo de la clase padre.
        print('Vuela pato')
        

pato = Pato()
pato.vuela()# aqui se ejecuta el metodo de la clase Pato
