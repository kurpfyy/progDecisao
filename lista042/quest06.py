"""
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”
"""

ANO1 = int(input("Me informe seu ano de nascimento: "))
ANO2 = int(input("Me informe o seu ano atual: "))

sum = ANO2 - ANO1

if (ANO1 > ANO2):
    print("Dados inseridos estão incorretos")

else:
    print(f"Sua idade é {sum}")