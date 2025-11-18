"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"

"""

peso = float(input("Digite seu peso em kg usando ponto (.) para separar os decimais: "))
altura = float(input("Digite sua altura em metros usando ponto (.) para separar metros e centímetros: "))

imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Atenção! Você está abaixo do peso ideal."
elif imc < 25:
    classificacao = "Parabéns! O seu peso está normal."
elif imc < 30:
    classificacao = "Atenção! Você está com sobrepeso."
else:
    classificacao = "Atenção! Você está obeso."

print(f"Classificação: {classificacao}")











#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝