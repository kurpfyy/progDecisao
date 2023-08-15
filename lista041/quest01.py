"""
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
"""

num= float(input("Me diga um numero"))

if (num > 20 ):
    sum = num / 2
    print(f"a metade do valor {num} é {sum} ")
else:
    print(f"O 1Numero inserido foi {num}")