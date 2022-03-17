from distutils.command.upload import upload
from pyexpat import model
from re import T
from sre_parse import State, Verbose
from tabnanny import verbose
from tokenize import blank_re
from django.db import models
from datetime import datetime

from importlib_metadata import method_cache

class Type(models.Model):

    name = models.CharField(max_length=150, verbose_name='Nombres', unique=True)

    def __str__(self):
        return str(self.id)

    #dedicarle ciertas propiedades a la entidad
    class Meta:

        verbose_name = 'Tipo'
        verbose_name_plural ='Tipos'
        #Que me lo acomode en Orden     
        ordering = ['id']
        
class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.names

    #dedicarle ciertas propiedades a la entidad
    class Meta:

        verbose_name = 'Category'
        verbose_name_plural ='Categorias'
        #Que me lo acomode en Orden     
        ordering = ['id']
        

class Employee(models.Model):
    
    #CASCADE si se llgara a eliminar la clase Type siguiera con el codigo
    #PROTECTED proteger la clase 
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    #Category sirve para enlazar dos tablas con diferente caregoria en el mismo type
    categ = models.ManyToManyField(Category)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    data_created = models.DateTimeField(auto_now=True)
    data_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    age = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    State = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%M/%D', null=True, blank=True)
    cvc = models.FileField(upload_to='cvc/%Y/%M/%D', null=True, blank=True)

    #Metodo str es la representacion del metodo to string
    # es decir cual es el atributo que va remplazar esos nombres.
    def __str__(self):
        return self.names

    #dedicarle ciertas propiedades a la entidad
    class Meta:

        verbose_name = 'Empleado'
        verbose_name_plural ='Empleados'
        db_table = 'empleado'
    #Que me lo acomode en Orden     
        ordering = ['id']
        

