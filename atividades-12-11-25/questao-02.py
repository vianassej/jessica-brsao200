"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""


"""
produto = "Camiseta"
preco = 50.00
desconto_percentual = 20

valor_desconto = (desconto_percentual / 100) * preco
preco_final = preco - valor_desconto
print("Produto: {}".format(produto))
print("Preço original: R$ {:.2f}".format(preco))
print("Desconto: {}%".format(desconto_percentual))
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço final: R$ {:.2f}".format(preco_final))

"""

produto = "Camiseta"
preco = input("Digite o preço da camiseta: ")
desconto_percentual = input("Digite a porcentagem de desconto: ")
valor_desconto = (float(desconto_percentual) / 100) * float(preco)
preco_final = float(preco) - valor_desconto
print("Produto: {}".format(produto))
print("Preço original: R$ {:.2f}".format(float(preco)))
print("Desconto: {}%".format(desconto_percentual))
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço final: R$ {:.2f}".format(preco_final))







#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝