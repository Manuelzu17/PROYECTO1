class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class Camieon():
    
    def desplazamiento(self):
        print("Me desplazo usando 10 ruedas")
        
def desplazamientoVegiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camieon()
desplazamientoVegiculo(miVehiculo)