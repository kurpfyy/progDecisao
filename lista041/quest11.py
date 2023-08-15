"""
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas
"""

numero = int(input("Digite um número inteiro de 3 algarismos: "))

if ( numero >= 100 and numero <= 999)
    centena = num // 100
    print(f"O algarismo das centenas de {numero} é {centena}")
else:
    print(f"O valor informado não possui 3 algarismo")
