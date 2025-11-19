"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

"""

dias_no_ano = 365
meses_no_ano = 12
try:
    dia_atual = int(input("Digite o dia atual (1-31): "))
    mes_atual = int(input("Digite o mês atual (1-12): "))
    ano_atual = int(input("Digite o ano atual (ex: 2024): "))

    dia_nascimento = int(input("Digite o dia de nascimento (1-31): "))
    mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))
    ano_nascimento = int(input("Digite o ano de nascimento (ex: 1990): "))

    anos_vividos = ano_atual - ano_nascimento
    meses_vividos = mes_atual - mes_nascimento
    dias_vividos = dia_atual - dia_nascimento

    if dias_vividos < 0:
        dias_vividos += 30
        meses_vividos -= 1

    if meses_vividos < 0:
        meses_vividos += meses_no_ano
        anos_vividos -= 1

    total_dias_vividos = (anos_vividos * dias_no_ano) + (meses_vividos * (dias_no_ano // meses_no_ano)) + dias_vividos

    print(f"Você está vivo há aproximadamente {total_dias_vividos} dias.")

except ValueError:
    print("Digite números válidos para dia, mês e ano.")


    





#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝