"""
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos
"""

id = int(input("Me informe sua idade"))

if (id < 18):
    (print("Você é menor de idade"))

if (id > 65):
    (print("Você tem mais de 65 anos"))

if (id > 18 and id < 65):
    (print("Você é maior de idade"))

