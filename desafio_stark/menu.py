from funciones import *

def mostrar_menu1():
    print(" * * * Menú de opciones: * * * ")
    print("-------------------------------")
    print("1 - Mostrar los nombres de cada supehéroe")
    print("2 - Mostrar altura y nombre")
    print("3 - Mostrar altura máxima")
    print("4 - Mostrar altura mínima")
    print("5 - Mostrar promedio de alturas")
    print("6 - Mostrar superhéroe más alto")
    print("7 - Mostrar superhéroe más bajo")
    print("8 - Mostrar superhéroe más pesado")
    print("9 - Mostrar superhéroe menos pesado")
    print("10 - Siguiente página")
    print("11 - Salir")
    print("-------------------------------")

def mostrar_menu2():
    print(" * * * Menú de opciones: * * * ")
    print("-------------------------------")
    print("12 - Mostrar nombres de superhéroes género M")
    print("13 - Mostrar nombres de superhéroes género F")
    print("-------------------------------")

def seguir_salir():
    continuar_salir = input("¿Desea salir? s/n")
    while continuar_salir != "s" and continuar_salir !="n":
        continuar_salir = input("ERROR, ingrese una opción válida. ¿Desea salir? s/n")
    if continuar_salir == "s":
        quit()


def elegir_opcion():
    mostrar_menu1()
    x = input("Ingrese una opción: ")
    match(x):
        case "1":
            mostrar_nombres()
        case "2":
            mostrar_nom_y_altura()
        case "3":
            altura_maxima, personaje_con_altura_maxima = encontrar_altura_maxima()

            print("Altura máxima encontrada:", altura_maxima)
            print("Personaje con altura máxima:", personaje_con_altura_maxima)
        case "4":
            altura_minima, personaje_con_altura_minima = encontrar_altura_minima()

            print("Altura mínima encontrada:", altura_minima)
            print("Personaje con altura mínima:", personaje_con_altura_minima)
        case "5":
            promedio_altura()
        case "6":
            encontrar_super_mas_alto()
        case "7":
            encontrar_super_mas_bajo()
        case "8":
            peso_maximo, personaje_con_peso_maximo = encontrar_peso_maximo()

            print("Peso máximo encontrado:", peso_maximo)
            print("Personaje con peso máximo:", personaje_con_peso_maximo)
        case "9":
            peso_minimo, personaje_con_peso_minimo = encontrar_peso_minimo()

            print("Peso mínimo encontrado:", peso_minimo)
            print("Personaje con peso mínimo:", personaje_con_peso_minimo)
        case "10":
            mostrar_menu2()
        case "11":
            seguir_salir()
        case "12":
            mostrar_nombres_M()
        case "13":
            mostrar_nombres_F()




while True:
    elegir_opcion()
