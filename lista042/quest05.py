"""
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
"""

est = input("Me informe a sigla de um estado brasileiro: ")

MG = "MG"
RJ =  "RJ"
SP = 'SP'
ES = 'ES'

if (est == MG or est == RJ or est == SP or est == ES ):
    print("O Estado Digitado esta na região Sudeste")

else:
    print("O Estado Informado Não esta na região Sudeste")