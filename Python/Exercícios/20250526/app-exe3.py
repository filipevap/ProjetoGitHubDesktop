'''3 - Solicite ao usuário o nome do estudante e 3 notas, retorne
a média ponderada das notas (com pesos 1,1 e 2), o nome
do estudante e se reprovado (media 6 aprovado).'''

nome=input("Informe o nome do estudante?\n")
nota1=int(input("\nInforme a nota do 1ª Trimestre\n"))
nota2=int(input("\nInforme a nota do 1ª Trimestre\n"))
nota3=int(input("\nInforme a nota do 1ª Trimestre\n"))

nota1=nota1*1
nota2=nota2*1
nota3=nota3*2

media=(nota1+nota2+nota3)/4

if media >= 6:
    print(f"\nO alunto {nome} foi APROVADO com nota {media}")
else:
    print(f"\nO alunto {nome} foi REPROVADO com nota {media}")
