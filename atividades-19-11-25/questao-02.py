"""
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. 
exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
API: https://randomuser.me/api/

"""
import requests
response = requests.get('https://randomuser.me/api/')
if response.status_code == 200:
    dados = response.json()['results'][0]
    nome = f"{dados['name']['first']} {dados['name']['last']}"
    email = f"{dados['email']}"
    pais = f"{dados['location']['country']}"
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")
else:
    print("Erro ao conectar à API.")   
         
         
         







#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝