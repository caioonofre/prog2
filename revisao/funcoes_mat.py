def cria_matriz(linhas, colunas):
    import random

    matriz = []
    for i in range(linhas):
        linha = [random.randint(0, 100) for j in range(colunas)]
        matriz.append(linha)
    return matriz


def soma_linha(matriz):
    soma = []
    for linha in matriz:
        soma.append(sum(linha))
    return soma


def maior_menor_matriz(matriz):
    maior = max(max(linha) for linha in matriz)
    menor = min(min(linha) for linha in matriz)
    return maior, menor


def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end=" ")
        print()


def transpoe_matriz(matriz):
    transposta = []
    for j in range(len(matriz[0])):
        linha_transposta = [matriz[i][j] for i in range(len(matriz))]
        transposta.append(linha_transposta)
    return transposta
