'''
#objeto fijo
class celular():
    #atributos estaticos, en todo va a ser lo mismo
    marca = "Samnsung"
    modelo = "S20"
    color = "azul"

celular1 = celular() #instanciar un objeto  - objeto 
celular2 = celular()

print(celular1.color)
#no se puede cambiar nada'''

#propiedades
class celular():
    #Metodo especial que se llama constructor, se va a ejecutar siempre
    def __init__(self, marca, modelo, color):#hace referencia hacia el mismo
        self.marca = marca
        self.modelo = modelo 
        self.color = color 

    #Metodos: funciones. Son para definir las acciones de un objeto 

    def llamar(self):
        print(f'estas haciendo un llamado de emergencia, desde un: {self.modelo}') #con el self se autoreferencia
    
    def colgar(self):
        print("colgaste")

celular1 = celular("Samsung", "S2O", "verde")
#print(celular1.color)
celular1.llamar()