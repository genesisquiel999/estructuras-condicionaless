nombre = input("Ingresa tu nombre")
edad = int(input("Ingresa tu edad"))
nota1 = float(input("Ingrese la primera nota"))
nota2 = float(input("Ingrese la segunda nota"))
nota3 = float(input("Ingrese la tercera nota"))
Promedio = (nota1 + nota2 + nota3 )/3
if Promedio >= 71:
    print("aprobado")
else:
    print("reprobado")