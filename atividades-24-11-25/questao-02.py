"""
2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, 
que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, 
caso ocorra um erro ao salvar, mostre uma mensagem de falha. 

"""

import csv

def criar_csv():
    pessoas = [
        {"nome": "Ana", "idade": 25, "cidade": "Rio de Janeiro"},
        {"nome": "Elaine", "idade": 30, "cidade": "São Paulo"},
        {"nome": "Maria", "idade": 22, "cidade": "Belo Horizonte"},
        {"nome": "Jessica", "idade": 32, "cidade": "Rio de Janeiro"},
        {"nome": "Carita", "idade": 28, "cidade": "Vitória"},
    ]

    nome_arquivo = input("Digite o nome do arquivo CSV para salvar (ex: pessoas.csv): ")

    try:
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["nome", "idade", "cidade"])
            
            escritor.writeheader()
            
            escritor.writerows(pessoas)

        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"Falha ao salvar arquivo: {e}")

criar_csv()



#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝