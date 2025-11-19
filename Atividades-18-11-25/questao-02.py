"""
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

"""
import string
def eh_palindromo(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    texto = texto.replace(" ", "")
    return texto == texto[::-1]
entrada = input("Digite uma palavra: ")
if eh_palindromo(entrada):
    print("Sim")
else:
    print("Não")
   













#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝