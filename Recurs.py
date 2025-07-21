def MENU():
    print("Bienvenido al Menu")
    print("1.Factorial")
    print("2.Suma primeros números naturales")
    print("3.Código de fibbonacci")
    print("4.Veces que se repite letra en palabra")
    print("5.Invertir cadena de texto")
    print("6.Potencia de un número")
    print("7.Salir")
allow = False
try:
    while allow == False:
        MENU()
        opt = int(input("Ingrese la opción que desee: "))
        match opt:
            case 1:
                print("Inicio")
            case 2:
                print("Inicio")
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