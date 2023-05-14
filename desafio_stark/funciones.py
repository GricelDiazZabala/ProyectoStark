from data_stark import lista_personajes

# 00 ----------------------------------------------------

def mostrar_nombres():
    for superheroe in lista_personajes:
        print(superheroe["nombre"])

def mostrar_nom_y_altura():
    for superheroe in lista_personajes:
        print("Nombre del superhéroe {}, altura {} cms".format(superheroe["nombre"], superheroe["altura"]))

def encontrar_altura_maxima():
    altura_maxima = 0
    personaje_con_altura_maxima = None

    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if altura > altura_maxima:
            altura_maxima = altura
            personaje_con_altura_maxima = personaje

    return altura_maxima, personaje_con_altura_maxima

def encontrar_altura_minima():
    altura_minima = float(lista_personajes[0]["altura"])
    personaje_con_altura_minima = None

    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if altura <= altura_minima:
            altura_minima = altura
            personaje_con_altura_minima = personaje

    return altura_minima, personaje_con_altura_minima

def promedio_altura():
    sum_altura = 0
    num_personajes = len(lista_personajes)
    for personaje in lista_personajes:
        sum_altura += float(personaje["altura"])
    promedio_altura = sum_altura / num_personajes

    print("La altura promedio de los superhéroes es: {} cms".format(promedio_altura))

    return promedio_altura

def encontrar_super_mas_alto():
    altura_maxima = 0
    personaje_con_altura_maxima = None

    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if altura > altura_maxima:
            altura_maxima = altura
            personaje_con_altura_maxima = personaje

    print("El superhéroe con la altura más alta es: {}".format(personaje_con_altura_maxima["nombre"]))

    return altura_maxima, personaje_con_altura_maxima

def encontrar_super_mas_bajo():
    altura_minima = float(lista_personajes[0]["altura"])
    personaje_con_altura_minima = None

    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if altura <= altura_minima:
            altura_minima = altura
            personaje_con_altura_minima = personaje

    print("El superhéroe con la altura más baja es: {}".format(personaje_con_altura_minima["nombre"]))

    return altura_minima, personaje_con_altura_minima

def encontrar_peso_maximo():
    peso_maximo = 0
    personaje_con_peso_maximo = None

    for personaje in lista_personajes:
        peso = float(personaje["peso"])
        if peso > peso_maximo:
            peso_maximo = peso
            personaje_con_peso_maximo = personaje

    return peso_maximo, personaje_con_peso_maximo

def encontrar_peso_minimo():
    peso_minimo = float(lista_personajes[0]["altura"])
    personaje_con_peso_minimo = None

    for personaje in lista_personajes:
        peso = float(personaje["peso"])
        if peso <= peso_minimo:
            peso_minimo = peso
            personaje_con_peso_minimo = personaje

    return peso_minimo, personaje_con_peso_minimo


# 01 ----------------------------------------------------

def mostrar_nombres_M():
    for superheroe in lista_personajes:
        if superheroe["genero"] == "M":
            print(superheroe["nombre"])

def mostrar_nombres_F():
    for superheroe in lista_personajes:
        if superheroe["genero"] == "F":
            print(superheroe["nombre"])