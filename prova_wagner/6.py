def soma_diagonal_principal_a(matriz):
    soma = 0
    for i in range (len(matriz)):
        soma += matriz[i][i]
    return soma

def soma_diagonal_principal_b(matriz):
    soma = 0
    for i in range (len(matriz)):
        soma += matriz[i][-i]
    return soma

def soma_diagonal_principal_c(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

def soma_diagonal_principal_d(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][len(matriz) - i - 1]
    return soma

def soma_diagonal_principal_e(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[len(matriz) - i - 1][i]
    return soma

matriz = [
    [5, 8, 12],
    [9, 3, 6],
    [7, 14, 2]
]

