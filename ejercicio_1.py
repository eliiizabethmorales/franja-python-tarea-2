# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase. 


def main():
    frase = input("hola , ingrese una frase: ")
    letra = input("ingrese la letra que quiere contar: ")
    contador = 0
    for numero in frase:
        if numero == letra:
            contador += 1
            print("la letra "+ letra + " se repite  "+  str(contador)+" en la frase " + frase + " .")
if __name__ == '__main__':
    main()
