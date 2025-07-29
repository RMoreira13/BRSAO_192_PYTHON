"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""
import requests
from datetime import datetime

def consultar_cotacao():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("Código de moeda inválido ou não encontrado.")
            return

        cotacao = dados[chave]
        valor_atual = float(cotacao["bid"])
        valor_max = float(cotacao["high"])
        valor_min = float(cotacao["low"])
        timestamp = int(cotacao["timestamp"])
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nCotação {moeda} para BRL:")
        print(f"Valor atual: R$ {valor_atual:.2f}")
        print(f"Valor máximo: R$ {valor_max:.2f}")
        print(f"Valor mínimo: R$ {valor_min:.2f}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
    except KeyError:
        print("Erro ao processar os dados. Verifique se o código da moeda está correto.")

consultar_cotacao()
