milista=["sebastian", 13, 1, 1995]

mitupla=tuple(milista)
print(mitupla)

milista=("sebastian", 13, 1, 1995)

mitupla=list(milista)
print(mitupla)

milista2=["sebastian", 15, 2, 1950]
mitupla2=list(milista2)
print(len(mitupla2))

mitupla2=("sebastian", 15, 2, 1950)
nombre, dia, mes, agno=mitupla2
print(nombre)
print(dia)
print(mes)
print(agno)