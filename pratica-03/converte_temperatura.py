"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""


valor = float(input("Digite o valor da temperatura: "))
origem = input("Informe a unidade de origem (C, F ou K): ").lower()
destino = input("Informe a unidade de destino (C, F ou K): ").lower()


if (origem != "c" and origem != "f" and origem != "k") or (destino != "c" and destino != "f" and destino != "k"):
    print("Unidades inválidas. Use apenas C, F ou K.")
else:
    
    if origem == destino:
        print(f"{valor}°{origem.upper()} = {valor:.2f}°{destino.upper()}")

    
    elif origem == "c" and destino == "f":
        resultado = (valor * 9 / 5) + 32
        print(f"{valor}°C = {resultado:.2f}°F")

   
    elif origem == "c" and destino == "k":
        resultado = valor + 273.15
        print(f"{valor}°C = {resultado:.2f}K")

    
    elif origem == "f" and destino == "c":
        resultado = (valor - 32) * 5 / 9
        print(f"{valor}°F = {resultado:.2f}°C")

    
    elif origem == "f" and destino == "k":
        resultado = (valor - 32) * 5 / 9 + 273.15
        print(f"{valor}°F = {resultado:.2f}K")

   
    elif origem == "k" and destino == "c":
        resultado = valor - 273.15
        print(f"{valor}K = {resultado:.2f}°C")

    
    elif origem == "k" and destino == "f":
        resultado = (valor - 273.15) * 9 / 5 + 32
        print(f"{valor}K = {resultado:.2f}°F")
