#Programa que pide la edad y el número de documento y verifica si la persona es mayor de 18 años
print("Bienvenido al sistema de verificación de requisitos de ingreso")
edad = int(input("Ingresa tu edad: "))
doc = (input("¿Tiene documento? SI(a), NO(b)"), True=="a", False=="b")

if edad>=18 or doc=="a":
    print("Puede entrar")
elif edad<=18 or doc=="b":
    print("no puede entrar")
else:
    print ("no puede entrar")