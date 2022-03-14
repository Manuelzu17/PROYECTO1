milista=["Manuel","Alejandra","Santiago","Maria",2]

print(milista[0:4])

milista.append("Camilo")

print(milista[:])

milista.extend(["sandra","Ana", "ramiro"])

print(milista.index("Maria"))#inserta el un elemento en la lista

milista.pop() #elimina el ultimo elemento de la lista
milista.remove(2)

print(milista[:])

milista2=["andrea","poto"]*3
milista3=milista+milista2

print(milista3[:])