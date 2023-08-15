"""
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
"""

not1=float(input("Qual sua nota do primeiro bimeste?"))
not2=float(input("Qual sua nota do segundo bimeste?"))
not3=float(input("Qual sua nota do terceiro bimeste?"))
not4=float(input("Qual sua nota do quarto bimeste?"))

sum = (not1 + not2 + not3 + not4) / 4

if (sum >= 5 ):
    print(f"Aprovado - Media: {sum}")
else:
    print(f"Reprovado - Media: {sum}")