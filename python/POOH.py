class vehiculos():
    
    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        
        self.enmarcha=True
    
    def acelerar(self):
        
        self.acelera=True
        
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print ("marca: ", self.marca, "\nModelo:", self.modelo, "\nEn Marcha",
               self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando" ,self.frena)
        
class furgoneta(vehiculos):
    
    def carga(self,cargar):
        self.cargado=cargar
        
        if(self.cargado):
            
            return "Lafurgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
        
class Moto(vehiculos):
    
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
        
    def estado(self):
        print ("marca: ", self.marca, "\nModelo:", self.modelo, "\nEn Marcha",
               self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando" ,self.frena, "\n", self.hcaballito)

class VElectricos(vehiculos):
    def __init__(self,marca, modelo):
        
        super().__init__(marca,modelo)
        self.autonomia=100
        
    def cargarEnergia(self):
        
        self.cargando=True        
    
miMoto=Moto("honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=furgoneta("Renault", "clio")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos, vehiculos): #La primera clase que se ponga al inicio es la principal
    
    pass

miBici=BicicletaElectrica("Orbe", "HC1030")
