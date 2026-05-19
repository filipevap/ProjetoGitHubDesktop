'''Crie um programa que:
Peça o nome do aluno
pea a idade
peça a nota
pergunte se ele entregou o trabalho (sim ou não)

Regras
1. se a idade for menor que 18, mostar que é menor de idade.
2. se for maior ou igual a 18, mostrar que é maior de idade.
3. mostrar se a idade é par ou ímpar
4. se a nota for 7 ou maior e entregou o trabalho, mostrar aprovado
5. se a nota for menor que 7 ou não entregou o trabalho, mostrar reprovado


'''

nome = input("Aluno, qual o seu nome?\n")

idade = int(input(f"\n{nome}, quantos anos você tem?\n"))
idade_resposta = "menor de idade" if idade < 18 else "maior de idade"
idade_par_impar = "par" if idade % 2 == 0 else "ímpar"

nota = float(input(f"\n{nome}, qual a nota que você tirou?\n"))

trabalho_entregue = input(f"{nome}, você entregou o trabalho? Responda com Sim ou Não.\n")
trabalho_condicao = True if trabalho_entregue.lower() == "sim" else False


if trabalho_condicao and nota >= 7:
    print(f"\n{nome}, a quantidade de anos que você tem é {idade_par_impar} e vocé é {idade_resposta}.\nAlém disso, você está APROVADO!")
else:
    print(f"\n{nome}, a quantidade de anos que você tem é {idade_par_impar} e vocé é {idade_resposta}.\nAlém disso, você está REPROVADO!")