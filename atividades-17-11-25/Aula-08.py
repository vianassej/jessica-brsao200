"""try:
    numerador = 10
    denominador = 0
    print(numerador/denominador)
except ZeroDivisionError:
    print("Você tentou dividir um número por 0.")
finally:
    print("Chegamos ao final do código")
"""
"""
Recaptulando:
nome = "Jéssica"
idade = 32
dando_aula = true 
altura = 1.50
frutas = ["abacaxi", "laranja", "morango", "uva"]

# Aula de Estrutura de Repetição
# Laço "FOR"
# listas, strings, intervalos, etc

#Exemplo de uso do for para iterar sobre uma lista

frutas = ["abacaxi", "laranja", "morango", "uva"]

print("abacaxi")
print("laranja")
print("morango")


for fruta in frutas:
    print(fruta)

 
for numero in range(10,50):
    print(numero)


# break e continue -> interrompe o codigo

#usando o break para interromper o laço 
"""
"""
for numero in range(1,11):
    if numero == 6:
        continue
    print(numero)

for numero in range(1,11):
    if numero == 6:
        break
    print(numero)


for numero in range(1,11):
    if numero % 2 != 0: # imprime só os números pares
        continue
    print(numero)
"""

# Try e Except
# try: tenta executar um bloco de código
# Except: Captura e trata erros que ocorrem no bloco try  

"""
try:
    #código que pode gerar um erro
    numero = int(input("Digite um número: "))
except ValueError:
    # código que será executado em caso de erro
    print("Valor inválido! Por favor, insira um número.")

"""


while True:
    senha = input("Digite a sua senha (ou 'sair' para encerrar): ")

    if senha.lower() == "sair":  # lower deixa tudo minúsculo
        print("Programa encerrado")
        break
    
    tem_oito_caracteres = len(senha) >= 8  # len vem de length (comprimento)
    
    tem_numero = any(caractere.isdigit() for caractere in senha)

    eh_forte = tem_oito_caracteres and tem_numero

    if eh_forte:
        print("Parabéns, sua senha é forte!")
        break
    else:
        print("Que pena, sua senha está fraca.")
        
        # Aqui dentro do else mostramos os motivos
        if not tem_oito_caracteres:
            print("A senha tem que ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("A senha tem que ter pelo menos 1 número.")
