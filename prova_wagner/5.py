def tem_duplicados1(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def tem_duplicados2(lista):
    lista_ordenada = sorted(lista)
    for i in range (len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
    return False

def tem_duplicados3(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False

lista = [3, 2, 7, 1, 4]

tem_duplicados1(lista)
tem_duplicados2(lista)
tem_duplicados3(lista)