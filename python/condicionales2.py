print("Programa de becas año 2022")
distancia_escuela=int(input("Introduce la distancia a la escuela en km"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el n de hermanos"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto"))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
 
    print("tienes derecho a beca")
    
else:
    
    print("No tiene derecho a la beca")
