import time

class Mapache:
    
    color  = "Undefined"
    raza   = "Undefined"
    tamano = "Undefined"
    
    def __init__(self,color,raza,tamano):
        self.color = color
        self.raza  = raza
        self.tamano = tamano
	
    def grunir(self):
        print("rrrrrr")

    def morder(self):
        print("Mordiendo")
    
    def agarrar(self):
        print("Agarrando objetos")

    def moverse(self):
        print("Moviendose")

a = int(input("Ingresa el número:"))
mapache = Mapache ("Gris","Boreal","Mediano")

ini = time.time()
for x in range(a):
	mapache.agarrar()
end = time.time()
print("Termina en ", (end-ini)*10000, "milisegundos")

ini = time.time()
for x in range(a):
	mapache.moverse()
end = time.time()
print("Termina en ", (end-ini)*10000, "milisegundos")

#Conclusion
#Se creo dos variables para ver como me arrojo un resultado mas rapido en agarrar a moverse por el usuario
