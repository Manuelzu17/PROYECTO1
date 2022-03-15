class Coche():
    
    def __init__(self):
        
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=True
    
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        
        if(self.enmarcha):
            chequeo=self.chequeo_interno()
            
        if(self.enmarcha and chequeo):
            return "el coche esta en marche"
        
        elif(self.enmarcha and chequeo==False):
            return "Algo a ido mal con el checkeo. no podemos arrancar"
            
        else:
            return "El coche esta parado"
           
    def estado(self):
        print("El coche tiene", self.ruedas, "ruedas. Un ancho de", self.anchoChasis, "y un largo de", 
              self.largoChasis)
        
    def chequeo_interno(self):
        print("realizando chequeo interno")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

            return True

        else:
            
            return False

micoche=Coche()

print(micoche.arrancar(True))
print(micoche.chequeo_interno())

print("----------A continuacion creamos otro coche----------------")

micoche2=Coche()

print(micoche2.arrancar(False))
print(micoche2.chequeo_interno())

micoche2.ruedas=6

micoche.estado()