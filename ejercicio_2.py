# Escribir una función que calcule el área de un círculo 
# y otra que calcule el volumen de un cilindro usando la primera función.

from cmath import pi


def area_circulo(radio):
    pi = 3.141592
    return pi*radio**2
def main():
    radio = int(input("ingrese el radio del circulo que quiere calcular: "))
    altura = int(input("si quiere saber el volumen del cilindro ingrese altura: "))
    area_circulo = pi*radio**2
    print("el area del circulo es "+str(area_circulo)+".")
    volumen_cilindro = area_circulo*altura
    print("el volumen del cilandro  es "+str(volumen_cilindro)+"")
    return area_circulo
    
if __name__ == '__main__':
    main()