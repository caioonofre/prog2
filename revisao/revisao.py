def convert_inteiro(text = "Insira um numero inteiro: "):
	while True:
		inteiro = input(text)
		try:
			inteiro = int(inteiro)
		except:
			print("Caractere digitado não é um número, digite um numero valido")
		else:
			return inteiro

def limpar_tela():
    import os
    input("Pressione ENTER para limpar…")
    os.system('cls' if os.name == 'nt' else 'clear')

    
#list compreessions
def criar_lista():
	a = [x for x in range(1, 11) if x % 2 == 0]
	print(f'Lista feita em list compreenssions {a}')

# solicitar um numero e imprimir diferentes formas
def solicitar_um_numero_e_imprimir():
	num = convert_inteiro()

	for i in range(1, num+1):
		print(f'{i} ' * i)
		
	for i in range(1, num+1):
		for j in range(1, i+1):
			print(j, end=" ")
		print()

def valor_maximo_e_minimo():
	maximo = 0
	minimo = 99999999
	for i in range(1, 6):
		valor = int(input(f"Insira o valor do deposito n° {i}: "))
		if valor > maximo:
			maximo = valor
		if valor < minimo:
			minimo = valor
		
	print(f'O depósito com valor mais alto foi: {maximo} e o depósito com o menor valor foi: {minimo}')	
	
solicitar_um_numero_e_imprimir()
a = input("quer limpar a tela? ")
if a == "S":
	limpar_tela()


