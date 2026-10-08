#  gerar_array: função que deverá receber por parâmetro um número que será o tamanho do array gerado e devolver um array de inteiros aleatórios (use a biblioteca random)

def gerar_array(tamanho):
    import random
    array = [random.randint(1, 100) for _ in range(tamanho)]   
    return array

# - soma_array: função que deverá receber por parâmetro um array e devolver o somatório dos valores do array.

def soma_array(array):
    soma = 0
    for i in range(len(array)):
        soma += array[i]
    return soma

# - media_array: função que deverá receber por parâmetro um array e devolver a média dos valores do array.

def media_array(array):
    soma =  0
    for i in range(len(array)):
        soma += array[i]
    media = soma / len(array)
    return media

# - inverte_array: função que deverá receber por parâmetro um array e devolver um array com os elementos invertidos (de trás para frente). Não use a função reverse. Crie sua própria.

def inverte_array(array):
    array_invertido = []
    for i in range(len(array)-1, -1, -1):
        array_invertido.append(array[i])
    return array_invertido

# - imprime_array: imprime elemento por elemento, um embaixo do outro.
def impreme_array(array)
    for i in array:
        print(i)

# - maior_array: função que deverá receber por parâmetro um array e devolver o maior dos valores do array. Crie a sua própria função. Não use bibliotecas.

def maior_array(array):
    maior = array[0]
    for i in array:
        if i > maior:
            maior = i
    return maior


# - menor_array: função que deverá receber por parâmetro um array e devolver o menor dos valores do array. Crie a sua própria função. Não use bibliotecas.

def menor_array(array):
    menor = array[0]
    for i in array:
        if i < menor:
            menor = i
    return menor

# Ao final,  imprima na tela:
# - o array
# - o array invertico
# - a soma
# - a média
# - menor valor
# - maior valor 
