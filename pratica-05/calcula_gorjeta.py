"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""

def gorjeta (valor_conta, porcentagem_gorjeta):
    calcula_gorjeta = valor_conta * (porcentagem_gorjeta/100)
    return calcula_gorjeta

valor_gorjeta = gorjeta(100, 15)
print(f"O valor da gorjeta é : R$ {valor_gorjeta:.2f}")
print(f"O total a ser pago é : R$ {100 + valor_gorjeta:.2f}")