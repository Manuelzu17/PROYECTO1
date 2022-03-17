from codecs import namereplace_errors
from multiprocessing.connection import Listener
from os import name
from web_project.wsgi import *
from core.erp.models import *
#Listar

#select *  from tabla 

#query = Type.objects.all()
#print(query)

#insertions

#tipe = Type(name='Manuel')
#tipe.name = 'pruebas'
#tipe.save()

#Observar el objeto deseado segun el id

#tipe = Type.objects.get(id=1)
#print(tipe.name)

# #edicion

#tipe = Type.objects.get(id=1)
#tipe.name = 'Actuiodsabn'
#tipe.save()

#eliminacion

#tipe = Type.objects.get(id=1)
#tipe.delete()

# buscar no importa su esta en mayusculas

#tipe = Type.objects.filter(name__icontains='manuel')
#print(tipe)

#LISTAR UTILIZANDO FILTROS

#name__contains = LIKE
#obj = Type.objects.filter(name__contains='Presidente')

#TOMAR MINUSCULA Y MAYUSCULAS

#obj = Type.objects.filter(name__icontains='manuel')

#IN

#obj = Type.objects.filter(name__in =['Manuel','jdsfosuib']).count()

#REGEXP

#obj = Type.objects.filter(name__iregex ='Aux')

#NO INT

#obj = Type.objects.filter(name__in =['Accionista','Presidente']).exclude(id=1)

#VER EL QUERY QIE EJECUTA LA SENTENCIA

#obj = Type.objects.filter(name__iregex ='Aux').query
#print(obj)

# #EMPLEADOS CON SON DEL TIPO 1

#obj = Employee.objects.filter(type_id=1)

#ITERAR

#for i in Type.objects.filter():
#    print(i.name)
    
#ITERAR
#for i in Type.objects.filter():
#    print(i.name+'-'+i.cate.name)

#INSERTAR CATEGORIA
 #t = Category()
 #t.name = 'Legumbres'
 #t.save()

#INGRESAR VARIOS 
#data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
 #        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
  #       'Grasas, aceite y mantequilla']

#for i in data:
    
   # cat = Category(name=i)
    #cat.save()
    #print('Guardado registro N°{}'.format(cat.id))

