"""
3 - Crie um programa que consulte informações de um  na API , 
retorne logradouro, bairro, cidade e estado do CEP digitado, 
caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

Api utilizada: https://viacep.com.br/

"""



import requests

cep = input("Digite o CEP: ")
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

if response.status_code == 200:
    dados = response.json()
    if "erro" not in dados:
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("CEP não encontrado.")
else:
    print("Erro ao conectar à API.")










#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝