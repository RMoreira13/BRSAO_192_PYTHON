"""1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.T
"""
import string as st
import numpy as np

quantidadeAlgorismos = int(input("Escolha quantos algorismos prefere para gerar a senha 8, 12 ou 16: "))
letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
algorismos = (letras+numeros+especial)

senha = np.random.choice(list(algorismos),quantidadeAlgorismos)
print("".join(senha))