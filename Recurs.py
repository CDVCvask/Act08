def MENU():
    print("Bienvenido al Menu")
    print("1.Factorial")
    print("2.Suma primeros números naturales")
    print("3.Código de fibbonacci")
    print("4.Veces que se repite letra en palabra")
    print("5.Invertir cadena de texto")
    print("6.Potencia de un número")
    print("7.Salir")
def Fact(n):
    if n == 0:
        return 1
    else:
        return n * Fact(n-1)
def Nat(n):
    if n == 1:
        return 1
    else:
        return n + Nat(n-1)
def Fibo(n):
    if n == 0:
        return 1
    else:
        return n + Fibo(n-1)
allow = False
try:
    while allow == False:
        MENU()
        opt = int(input("Ingrese la opción que desee: "))
        match opt:
            case 1:
                number = int(input("Ingrese el número del que desee ver el factorial: "))
                if number <= 0:
                    print("El valor ingresado no es valido")
                else:
                    print(Fact(number))
            case 2:
                number = int(input("Ingrese el número para sumar los naturales anteriores: "))
                if number <= 0:
                    print("El valor ingresado no es valido")
                else:
                    print(Nat(number))
            case 3:
                print("Inicio")
            case 4:
                print("Inicio")
            case 5:
                print("Inicio")
            case 6:
                print("Inicio")
            case 7:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Error:El valor ingresado no es valido")