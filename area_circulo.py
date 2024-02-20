import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = float(input("Ingresa el radio del círculo: "))

area_del_circulo = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area_del_circulo}")