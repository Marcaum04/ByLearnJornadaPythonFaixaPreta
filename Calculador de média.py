def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media
def verificar_aprovacao(media):
    if media >= 7:
        print("O aluno foi aprovado com a média", media)
    else:
        print("O aluno foi reprovado com a média", media)

nota_um = float(input("Digite sua primeira nota:" ))
nota_dois = float(input("Digite sua segunda nota:" ))

media_aluno = calcular_media(nota_um, nota_dois)

verificar_aprovacao(media_aluno)