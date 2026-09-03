from funcoes_mat import divisao, multiplicacao, potencia, raiz_quadrada, soma, subtracao

print("Arquivo de funções matemáticas importado com sucesso!")

print("Operações matemáticas disponíveis:")
print("- Soma")
print("- Subtração")
print("- Multiplicação")
print("- Divisão")

input("Pressione Enter para continuar...")
operacao = input(
    "Qual operação você deseja realizar? (Digite 'soma', 'subtracao', 'multiplicacao' ou 'divisao') digite 0 para sair: "
)

while operacao != "0":
    if operacao not in ["soma", "subtracao", "multiplicacao", "divisao", "0"]:
        print("Operação inválida. Por favor, escolha uma operação válida.")
    else:
        match operacao:
            case "soma":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"O resultado da soma é: {soma(a, b)}")
            case "subtracao":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"O resultado da subtração é: {subtracao(a, b)}")
            case "multiplicacao":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"O resultado da multiplicação é: {multiplicacao(a, b)}")
            case "divisao":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                try:
                    resultado = divisao(a, b)
                    print(f"O resultado da divisão é: {resultado}")
                except ValueError as e:
                    print(e)
            case "potencia":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"O resultado da potência é: {potencia(a, b)}")
            case "raiz_quadrada":
                a = float(input("Digite o número: "))
                try:
                    resultado = raiz_quadrada(a)
                    print(f"O resultado da raiz quadrada é: {resultado}")
                except ValueError as e:
                    print(e)

    operacao = input(
        "Qual operação você deseja realizar? (Digite 'soma', 'subtracao', 'multiplicacao' ou 'divisao') digite 0 para sair: "
    )
