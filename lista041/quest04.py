"""
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”
"""

num = int(input("Me diga um numero inteiro"))

div4 = num % 4
div5 = num % 5

if (div4 == 0 and div5 == 0 ):
    print(f"{num} é divisivel por 4 e 5 ao mesmo tempo")
else:
    print(f"{num} não é divisivel por 4 e nem 5")