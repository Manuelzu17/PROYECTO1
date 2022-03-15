from operator import ne


def generaPares(limite):
    
    num=1
    
    miLista=[]
    
    while num<limite:
        
        miLista.append(num*2)
        
        num=1+num
    
    return miLista

print(generaPares(10))

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento
        
devuelve_ciudades=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(devuelve_ciudades))
print(next(devuelve_ciudades))
print(next(devuelve_ciudades))