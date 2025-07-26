"""
2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.
"""

import unicodedata

def remover_acentos(texto):

    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join(
        c for c in texto_normalizado
        if unicodedata.category(c) != 'Mn'
    )
    return texto_sem_acentos

def verificar_palindromo(frase):
    frase = frase.lower()
    frase = remover_acentos(frase)

    caracteres_validos = ""
    for letra in frase:
        if letra.isalnum():
            caracteres_validos += letra

    return caracteres_validos == caracteres_validos[::-1]

entrada = input("Digite uma palavra ou frase: ")

if verificar_palindromo(entrada):
    print("Sim")
else:
    print("Não")
