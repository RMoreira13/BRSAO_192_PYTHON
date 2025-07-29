"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""

import requests

def consultar_cep():
    cep = input("Digite um CEP (apenas números, sem traço): ")

    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Certifique-se de digitar exatamente 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            return

        print("\nInformações do Endereço:")
        print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
        print(f"Bairro:     {dados.get('bairro', 'Não disponível')}")
        print(f"Cidade:     {dados.get('localidade', 'Não disponível')}")
        print(f"Estado:     {dados.get('uf', 'Não disponível')}")
        print(f"CEP:        {dados.get('cep', 'Não disponível')}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API do ViaCEP:", erro)

consultar_cep()

