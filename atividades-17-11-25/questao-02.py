"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.

"""

try:
    alunos = int(input("Digite o número de alunos: "))
    notas = []

    for i in range(alunos):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    print("\nNotas registradas:", notas)
    print("Média da turma:", media)

except ValueError:
    print("Tente novamente. Digite apenas números.")




















#╔═══════════════════════════╗
#║       </> vianassej       ║
#╚═══════════════════════════╝