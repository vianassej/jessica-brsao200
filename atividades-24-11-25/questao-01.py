"""
1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , 
calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo 
não exista ou houver erro na leitura, mostre uma mensagem de erro. 

"""

import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media_tempo:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        
nome_arquivo = input("Digite o nome do arquivo CSV de logs de treinamento: ")
processar_logs_treinamento(nome_arquivo)



#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝