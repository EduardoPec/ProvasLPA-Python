numero_alunos = int(input("Informe o número de alunos: "))
somador_medias = 0

for i in range(numero_alunos):
    nome = input("Digite seu nome: ")
    nota1 = float(input("Informe sua primeira nota: "))
    nota2 = float(input("Informe sua segunda nota: "))
    nota3 = float(input("Informe sua terceira nota: "))
    media = (nota1 + nota2 + nota3)/3
    somador_medias += media

    if media >= 7:
        print("=========================================================")
        print(f"Suas notas foram respectivamentes, {nota1}, {nota2} e {nota3}")
        print("---------------------------------------------------------")
        print(f"Parabéns {nome}, você está aprovado(a) com média: {media:.2f}!")
        print("=========================================================")
    else:
        print("=========================================================")
        print(f"Suas notas foram respectivamentes, {nota1}, {nota2} e {nota3}")
        print("---------------------------------------------------------")
        print(f"Infelizmente {nome}, você está reprovado(a) com média: {media:.2f}!")    
        print("=========================================================")

media_geral = somador_medias/numero_alunos
print("--------------------------------")
print(f"A média geral da turma é: {media_geral:.2f}")
print("--------------------------------")