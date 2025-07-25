"""
4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  
"""

total_pares = 0
total_impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print("Número par.\n")
            total_pares += 1
        else:
            print("Número ímpar.\n")
            total_impares += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.\n")

print("\nResumo:")
print(f"Total de números pares: {total_pares}")
print(f"Total de números ímpares: {total_impares}")
