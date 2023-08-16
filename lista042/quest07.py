"""
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
"""

num = int(input("Me informe um numero"))
num2 = int(input("Me Informe um numero"))

if (num > num2):
    print(f"O primeiro numero {num} é maior que {num2}")

if (num < num2):
    print(f"O Segundo numero {num2} é maior que {num}")

if (num == num2):
    print(f"Os Numeros são iguais")
    