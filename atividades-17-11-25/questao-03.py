"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.

"""


while True:
    try:
        senha = input("Digite a sua senha (ou 'sair' para encerrar): ")

        if senha.lower() == "sair":  # lower deixa tudo minúsculo
            print("Programa encerrado")
            break
        
        # Pelo menos 8 caracteres
        tem_oito_caracteres = len(senha) >= 8

        # Pelo menos 1 número
        tem_numero = any(caractere.isdigit() for caractere in senha)

        # Senha é forte se atender aos dois critérios acima
        eh_forte = tem_oito_caracteres and tem_numero

        if eh_forte:
            print("Parabéns, sua senha é forte!")
            break
        else:
            print("Que pena, sua senha está fraca.")
            if not tem_oito_caracteres:
                print("A senha tem que ter pelo menos 8 caracteres.")
            if not tem_numero:
                print("A senha tem que ter pelo menos 1 número.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        print("Tente novamente ou digite 'sair' para encerrar.")











#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝