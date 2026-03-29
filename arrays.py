def tiene_duplicados(array):
    vistos = set()
    for numero in array:
        if numero in vistos:
            return True
        vistos.add(numero)
    return False

def suman_target(array, target):
    vistos = {}
    for indice, numero in enumerate(array):
        complemento = target - numero
        if complemento in vistos:
            return [vistos[complemento], indice]
        vistos[numero] = indice

def repetidos(array):
    vistos = set()
    for numero in array:
        if numero in vistos:
            return numero
        vistos.add(numero)
    return -1

def suma(array, target):
    vistos = set()
    for numero in array:
        complemento = target - numero
        if complemento in vistos:
            return True
        vistos.add(numero)
    return False