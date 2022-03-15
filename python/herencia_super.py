from curses.ascii import EM


class Persona():
    
    def __init__(self, nombre, edad, Lugar_residencia):
        
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia
    
    def descripcion(self):
        
        print("nombre: ", self.nombre, "edad: ", self.edad, "residencia:", self.lugar_residencia)
        
class Empleado(Persona):
    
    def __init__(self, genero, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        
        self.genero=genero
        self.salario=salario
        self.antigüedad=antigüedad

    def descripcion(self):
    
        super().descripcion()
    
        print("Genero:", self.genero, "Salario:", self.salario, "antiguedad", self.antigüedad)    

Manuel=Empleado("m", 155, 5465, "Manuel", 55, "Colombia")
Manuel.descripcion()
print(isinstance(Manuel,Empleado))
