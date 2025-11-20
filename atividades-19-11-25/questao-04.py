"""
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando 
a API mostre valor atual, máxima, mínima e data/hora da última atualização, 
caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

Api: https://economia.awesomeapi.com.br/json/last/{MOEDA}-BRL
"""
import requests

def consultar_moeda(moeda: str):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{moeda.upper()}BRL" 
        if chave in dados:
            info_moeda = dados[chave]
            return {
                "valor_atual": info_moeda.get("bid"),
                "valor_maximo": info_moeda.get("high"),
                "valor_minimo": info_moeda.get("low"),
                "ultima_atualizacao": info_moeda.get("create_date")
            }
        else:
            return {"erro": f"Moeda '{moeda}' não encontrada."}

    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro na requisição: {e}"}

resultado = consultar_moeda("USD")  # exemplo: dólar
if "erro" in resultado:
    print(resultado["erro"])
else:
    print(f"Valor atual: {resultado['valor_atual']}")
    print(f"Máximo: {resultado['valor_maximo']}")
    print(f"Mínimo: {resultado['valor_minimo']}")
    print(f"Última atualização: {resultado['ultima_atualizacao']}")





#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝