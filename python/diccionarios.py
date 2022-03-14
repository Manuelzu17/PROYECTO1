from re import S


midiccionario={23:"jordan","Alemania":"Berlin","Francia":"Paris","Fechas":{1991,}}
midiccionario["Italia"]="lisboa"
midiccionario[("Italia")]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario.keys)
print(midiccionario.values)
print(len(midiccionario))