"""
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  
também escolha o tamanho da senha para criar senhas seguras automaticamente.

"""

import random
import string

def senhas_seguras (tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = senhas_seguras(tamanho_senha)
print("Senha gerada:", senha_gerada)

