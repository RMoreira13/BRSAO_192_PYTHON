"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

# Valores das notas
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Calcula média
soma_notas = nota1 + nota2 + nota3
media_notas = soma_notas / 3

# Média aluno
print("A nota1 é: {:.2f}".format(nota1))
print("A nota2 é: {:.2f}".format(nota2))
print("A nota3 é: {:.2f}".format(nota3))
print("A soma das notas é: {:.2f}".format(soma_notas))
print("A média final do aluno é: {:.2f}".format(media_notas))