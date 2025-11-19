"""
4 - Criar um código que serve para analisar números digitados pelo usuário, 
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

"""

try:

    total_pares = 0
    total_impares = 0

    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número: "))

        if numero % 2 == 0:
            total_pares += 1
        else:
            total_impares += 1

    print(f"Total de números pares: {total_pares}")
    print(f"Total de números ímpares: {total_impares}") 
            
except ValueError:
    print("Por favor, digite apenas números inteiros.")














#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝