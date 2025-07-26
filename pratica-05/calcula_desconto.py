"""
3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""

def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

preco = float(input("Digite o preço original do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

preco_com_desconto = calcular_desconto(preco, desconto)

print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")