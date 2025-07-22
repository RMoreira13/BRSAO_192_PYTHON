"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""
# Valores iniciais
produto1 = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calculo do desconto
valor_do_desconto = preco_original * (porcentagem_desconto / 100)
valor_com_desconto = preco_original - valor_do_desconto

# Valor com desconto
print("O valor original da {} é de R$ {:.2f} e a porcentagem de desconto é de {}%, concedendo um desconto de R$ {:.2f}. Dessa forma o valor final com desconto é de R$ {:.2f}.".format(produto1, preco_original, porcentagem_desconto, valor_do_desconto, valor_com_desconto))

