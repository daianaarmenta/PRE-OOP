'''#objeto fijo
class celular():
    #atributos estaticos, en todo va a ser lo mismo
    marca = "Samnsung"
    modelo = "S20"
    color = "azul"

celular1 = celular() #instanciar un objeto  - objeto 
print(celular1)
print(celular1.color)

celular2 = celular()
print(celular2)
print(celular2.color)
#no se puede cambiar nada'''

#propiedades
class celular():
    #Metodo especial que se llama constructor, se va a ejecutar siempre
    def __init__(self, marca, modelo, color, size, memoria):#hace referencia hacia el mismo
        self.marca = marca
        self.modelo = modelo 
        self.color = color
        self.size = size
        self.memoria = memoria 

    #Metodos: funciones. Son para definir las acciones de un objeto 
    def llamar(self):
        print(f'estas haciendo un llamado de emergencia, desde un: {self.modelo} {self.marca}') #con el self se autoreferencia
    
    def colgar(self):
        print("colgaste")

celular1 = celular("Samsung", "S2O", "verde","10 inch","128 GB")
celular2 = celular("Apple", "iphone 15", "rosa", "5 inch", "128 GB")
celular3 = celular("Huawei", "Honor", "azul", "4 inch", "64 GB")
print(celular1.marca,celular2.marca,celular3.marca)
celular1.llamar()