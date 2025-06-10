
print('Que figura desea calcular? \n 1.- Triangulo \n 2.- Cuadrado \n 3.- Circulo \n 4.- Rectángulo')

coso = input()

if coso == '1':
    print("Inserte la base y luego la altura")
    bs = int(input())
    h = int(input())
    print("El area de tu trangulo es:")
    print(bs*h/2)

if coso == '2':
    print("Inserte el lado de uno de los lados")
    ld = int(input())
    print("El area de tu cuadrado es:")
    print(ld*ld)

if coso == '3':
    print("Inserte el valor del radio")
    rd = int(input())
    print("El area de tu circulo es:")
    print(3.1416*(rd*rd))

if coso == '4':
    print("Inserte el valor de la base y luego de la altura")
    bd = int(input())
    h = int(input())
    print("El area de tu rectángulo es:")
    print(bd*h)