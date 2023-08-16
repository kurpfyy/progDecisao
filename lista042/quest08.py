"""
Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final
"""
num = float(input("Me informe um numero"))
num2 = float(input("Me Informe um numero"))
num3 = float(input("Me informe um numero"))

maior = num

if (maior < num2):
    maior = num2
    
if (maior < num3):
    maior = num3

print(f"O maior numero é {maior}")