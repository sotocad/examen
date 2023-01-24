import math
radio = float(input("Ingresa el radio: "))
diametro = radio * 2
circunferencia = "{:.6f}".format(diametro * math.pi)
print("La circunferencia es" , circunferencia,  "para un diametro de " ,diametro, "y radio de " ,radio)