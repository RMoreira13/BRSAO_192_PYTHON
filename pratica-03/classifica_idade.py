"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).
"""

idade = int(input("Digite sua idade:"))

if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print(f"Sua idade é {idade} anos, você é criança")
elif idade <= 17:
    print(f"Sua idade é {idade} anos, você é adolescente")
elif idade <= 59:
    print(f"Sua idade é {idade} anos, você é adulto")
else:
    print(f"Sua idade é {idade} anos, você é idoso")
