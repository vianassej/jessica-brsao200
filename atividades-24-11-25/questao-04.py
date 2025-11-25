"""
4 -   Crie um programa que leia e escreva arquivos no formato , 
que salve em um dicionário com nome, idade e cidade em um arquivo JSON 
e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, 
mostre uma mensagem de falha.

"""
import json

def salvar_e_ler_json():
    dados = {
        "nome": "Jéssica",
        "idade": 32,
        "cidade": "Rio de Janeiro"
    }

    nome_arquivo = input("Digite o nome do arquivo JSON para salvar (ex: dados.json): ")

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)
            print("Dados lidos do JSON:")
            print(f"Nome: {conteudo['nome']}")
            print(f"Idade: {conteudo['idade']}")
            print(f"Cidade: {conteudo['cidade']}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Falha ao salvar ou ler arquivo: {e}")

salvar_e_ler_json()


#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝
