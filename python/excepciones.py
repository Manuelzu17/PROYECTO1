import re


def multiplica(num1, num2):

    return num1*num2

def divide (num1,num2):
    
    try:
        return num1/num2
    
    except ZeroDivisionError:
        print("No se puede dividir entre zero")
        return "Operacion errona"
    
try:

    op1=(int(input("Introduce el primer numero:")))
    op2=(int(input("Introduce el segundo numero:")))
    
except ValueError:
    
    print("Introduce un valor numerico")


operacion=input("Introduce la operacion a realizar (multiplica y divide)")

         
try:
    
    if operacion=="multiplica":
     print(multiplica(op1,op2))

    elif operacion=="divide":
        print(divide(op1,op2))

except NameError:
     print("No introduciste un numero entero")