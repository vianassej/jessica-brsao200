"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).

"""

try:
    idade = int(input("Digite a sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Você é uma Criança!")

    elif idade >= 13 and idade <= 17:
        print("Você é um Adolescente!")

    elif idade >= 18 and idade <= 59:
        print("Você é um Adulto!")

    elif idade >= 60 and idade <= 110:
        print("Você é um Idoso!")

    else:
        print("Idade Inválida!")

except ValueError:
    print("Por favor, digite apenas números inteiros positivos.")









#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝