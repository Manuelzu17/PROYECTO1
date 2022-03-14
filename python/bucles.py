email=False
miEmail=input("Introduce tu direccion de email:")

for i in miEmail:
    
    if(i=="@"):
        
        email=True
if email:
    print("Email es correcto")
else:
    print("El email no es correcto")
    
for i in range(5):
    print(f"valor de la variable {i}")
    