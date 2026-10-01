# 4 -  Recebe uma string e Retorna a qtd de caracteries especiais (@#$%&_+=-?! etc.)
novaString = input("Digite uma string: ")
def contar_caracteres_especiais(string):
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;':\",.<>?/\\"
    contador = 0
    for char in string:
        if char in caracteres_especiais:
            contador += 1
    return contador

# 5 -  Recebe uma string e retorna um array com todos os índices das vogais, 
def encontrar_indices_vogais(string):
    vogais = "aeiouAEIOU"
    indices = []
    for i, char in enumerate(string):
        if char in vogais:
            indices.append(i)
    return indices

# 6 -  Recebe uma string e retorna um array com todos os índices das consoantes.
def encontrar_indices_consoantes(string):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    indices = []
    for i, char in enumerate(string):
        if char in consoantes:
            indices.append(i)
    return indices

# 7 -  Recebe uma string e retorna um array com todos os índices de todos os caracteres que são números.
def encontrar_indices_numeros(string):
    numeros = "0123456789"
    indices = []
    for i, char in enumerate(string):
        if char in numeros:
            indices.append(i)
    return indices

# 8 - Recebe uma string e gera um array com os números dessa string. Após isso, a função deve imprimir elemento por elemento do array  informando cada um se é par ou ímpar.
# Ex: se digitado pelo  usuário a string: "abc12345!?" deverá ser impresso na tela:
# 1 - impar
# 2 - par
# 3 - impar
# 4 - par
# 5 - impar