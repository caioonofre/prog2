def inverte_str(str_para_inverter):
    invertida = str_para_inverter[::-1]
    return invertida


def e_palindromo(pal):
    str_sem_espacos = pal.replace(" ", "").lower()
    return str_sem_espacos == inverte_str(str_sem_espacos)


def localiza_caracter(texto):
    letra = input("Digite uma letra para localizar: ")
    return letra in texto