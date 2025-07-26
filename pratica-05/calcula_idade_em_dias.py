"""
4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.
"""

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano = int(input("Digite o ano de nascimento: "))
dias = calcular_idade_em_dias(ano)

print(f"Você tem aproximadamente {dias} dias de vida.")
