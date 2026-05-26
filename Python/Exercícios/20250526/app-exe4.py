'''4 - Leia o ano de nascimento de uma pessoa e o ano atual.
Com base nisso, calcule a idade da pessoa e informe se ela é
maior de idade (18 anos ou mais) ou menor de idade.'''

born=int(input("Qual o ano em que você nasceu?\n"))
atual=int(input("Que ano estamos?\n"))

idade=atual-born

if idade>=18:
    print("Você é maior de idade\n")
else:
    print("Você é DE menor")    

