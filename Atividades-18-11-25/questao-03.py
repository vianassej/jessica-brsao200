"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

"""

calculo_desconto = lambda preco, percentual: preco * (percentual / 100)
preco_final = lambda preco, desconto: preco - desconto

try:
    preco_produto = float(input("Digite o preço do produto: R$ "))
    percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

    valor_desconto = calculo_desconto(preco_produto, percentual_desconto)
    novo_preco = preco_final(preco_produto, valor_desconto)

    print(f"O preço final após o desconto é: R$ {novo_preco:.2f}")

except ValueError:
    print("Digite números válidos.")           








#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝