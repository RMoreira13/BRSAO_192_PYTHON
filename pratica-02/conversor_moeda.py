"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

# Valores iniciais
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversão
valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro

# Exibição dos resultados
print("Valor em Reais: R$ {:.2f}".format(valor_reais))
print("Convertido em Dólares: US$ {:.2f}".format(valor_em_dolar))
print("Convertido em Euros: € {:.2f}".format(valor_em_euro))