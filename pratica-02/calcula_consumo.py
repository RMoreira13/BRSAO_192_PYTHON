"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""
# Valores iniciais
distancia = 300
combustivel_gasto = 25

# Consumo médio
consumo_medio = distancia / combustivel_gasto
 
 # Exibição dos resultados
print("A distância percorrida foi de {}km e o combustível gasto foi de {} litros. O consumo médio é de {:.2f} km/l".format(distancia, combustivel_gasto, consumo_medio))