"""
Crie um programa que pergunte um numero de usuario.
Em seguida o programa deve informar se o numero inserido esta abaixo de 100
"""

num = int(input("Informe um numero"))

if ( num < 100 ):
    print(f"{num} está abaixo de 100")
elif (num <= 200):
    print(f"{num} esta entre 100 e 200")
else:
    print(f"{num} esta acima de 200")