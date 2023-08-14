"""
Crie um programa que pergunte dois numeros ao usuario.
Em seguida o programa deverá somar os dois numeros e
apresentar o resultado se o valor for maior que 10
"""

num1 = int(input("Informe um numero"))
num2 = int(input("Informe outro numero"))

soma = num2 + num1

if (soma > 10):
    print(f"A soma dos valores inserido é = {soma}")

print("FIM DO PROGRAMA")