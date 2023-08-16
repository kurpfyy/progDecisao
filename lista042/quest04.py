"""
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana
"""

num = int(input("Me informe um numero de 1 a 7:"))

d1 = ("Segunda")
d2 = ("Terça")
d3= ('Quarta')
d4= ('Quinta')
d5= ('Sexta')
d6= ('Sabado')
d7= ('Domingo')

if (num < 1 ):
    print("Numero invalido")

if (num > 7):
    print("Numero invalido")

if (num == 1):
    print(f"O dia Da semana é {d1}")

if (num == 2):
    print(f"O dia Da semana é {d2}")

if (num == 3):
    print(f"O dia Da semana é {d3}")

if (num == 4):
    print(f"O dia Da semana é {d4}")

if (num == 5):
    print(f"O dia Da semana é {d5}")

if (num == 6):
    print(f"O dia Da semana é {d6}")

if (num == 7):
    print(f"O dia Da semana é {d7}")