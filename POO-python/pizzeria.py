class pizza():
    def __init__(self,nombre,size,toppings,salsa,queso,masa,orilla,precio):
        self.nombre = nombre
        self.size = size
        self.toppings = toppings
        self.salsa = salsa
        self.queso = queso
        self.masa = masa
        self.orilla = orilla
        self.precio = precio

orden1 = pizza("Hawaiana","mediana","piña y jamón","normal","normal","sartén","sin queso","$250")
orden2 = pizza("Pepperoni","grande","pepperoni","extra","extra","normal","con queso","$400")
orden3 = pizza("Sarachito","chica","champiñones y carne","extra","extra","sartén","con queso","$1000")

print(orden1.nombre,orden2.nombre,orden3.nombre)


