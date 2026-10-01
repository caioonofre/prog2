from funcoes_str import e_palindromo, inverte_str, localiza_caracter  # noqa: I001
from funcoes_mat import (
    cria_matriz,
    soma_linha,
    maior_menor_matriz,
    imprime_matriz,
    transpoe_matriz,
)

while True:
    print("Menu: \n0 ou E - Encerra o programa\n1 ou S - Texto\n2 ou M - Matriz")

    opcao = input("Escolha uma opção: ").strip().upper()

    if opcao in ["0", "E"]:
        print("Encerrando o programa...")
        break
    elif opcao in ["1", "S"]:
        while True:
            try:
                texto = input("Digite uma palavra ou frase: ").strip()
                if not texto:
                    raise ValueError("A entrada não pode estar vazia.")
                break
            except ValueError as e:
                print(e)

        invertida = inverte_str(texto)
        palindromo = e_palindromo(texto)
        letra_encontrada = localiza_caracter(texto)

        print(f"String invertida: {invertida}")
        print(f"É palíndromo: {'Sim' if palindromo else 'Não'}")
        print(
            f"Letra encontrada: {'Encontrou' if letra_encontrada else 'Não Encontrou'}"
        )

    elif opcao in ["2", "M"]:
        while True:
            try:
                linhas = int(input("Digite o número de linhas: "))
                colunas = int(input("Digite o número de colunas: "))
                if linhas <= 0 or colunas <= 0:
                    raise ValueError("O número de linhas e colunas deve ser positivo.")
                break
            except ValueError as e:
                print(e)

        matriz = cria_matriz(linhas, colunas)
        soma_linhas = soma_linha(matriz)
        maior, menor = maior_menor_matriz(matriz)
        transposta = transpoe_matriz(matriz)

        print("Matriz original:")
        imprime_matriz(matriz)

        print(f"Soma de cada linha: {soma_linhas}")
        print(f"Maior valor da matriz: {maior}")
        print(f"Menor valor da matriz: {menor}")

        print("Matriz transposta:")
        imprime_matriz(transposta)

    else:
        print("Opção inválida. Tente novamente.")
