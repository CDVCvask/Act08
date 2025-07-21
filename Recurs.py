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
    if n <= 0:
        return 0
    else:
        return n + Fibo(n-2)
def Back(List,n):
    if n == len(List):
        return list[n]
    else:
        return Back(List,n-1) + List[n]
def Power(B,Ex):
    if Ex == 0:
        return 1
    else:
        return B * Power(B,Ex-1)
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
                number = int(input("Ingrese el número para ver su fibbonacci: "))
                if number < 0:
                    print("El valor ingresado no es valido")
                else:
                    print(Fibo(number))
            case 4:
                word = input("Ingrese una palabra de texto: ")
                look = input("Ingrese la letra para ver cuántas veces se repite: ")
                parts = list(word)
            case 5:
                word = input("Ingrese una palabra de texto: ")
                parts = list(word)

            case 6:
               base = int(input("Ingrese la base: "))
               if base <= 0:
                   print("El valor ingresado no es valido")
               else:
                    ex = int(input("Ingrese la exponente: "))
                    if ex <= 0:
                        print("El valor ingresado no es valido")
                    else:
                        print(Power(base,ex))
            case 7:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Error:El valor ingresado no es valido")