"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

"""

while True:
    try:
        num1 = float(input("Digite o primeiro número (ou '0' para sair): "))
        if num1 == 0:
            print("Programa encerrado.")
            break

        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação ('+' para somar, '-' para subtrair, '*' para multiplicar ou '/' para dividir): ")

        if operacao == "+":
            print("Resultado:", num1 + num2)
        elif operacao == "-":
            print("Resultado:", num1 - num2)
        elif operacao == "*":
            print("Resultado:", num1 * num2)
        elif operacao == "/":
            try:
                print("Resultado:", num1 / num2)
            except ZeroDivisionError:
                print("Erro: não é possível dividir por zero.")
        else:
            print("Algo deu errado.")

    except ValueError:
        print("Algo deu errado. Digite apenas números.")











#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝