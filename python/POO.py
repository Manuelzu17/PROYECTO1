from cProfile import run


class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marche"
        else:
            return "El coce esta parado"
micoche=Coche()

print("El largo del coche es:", micoche.largoChasis)
print("El coche tiene, micoche", micoche.ruedas, "ruedas")

micoche.arrancar()

print(micoche.estado())