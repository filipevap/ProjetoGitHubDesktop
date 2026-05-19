'''04 Nota do Aluno
Peça a nota do aluno
Se for 10, mostre "Nota Máxima!"
Se for 7 ou mais, mostre "aprovado"
senão, reprovado Se estiver corret, mostre "acesso permitido" Senão Senha incorreta.'''

nota = float(input("Qual nota foi tirada pelo aluno?\n"))
print("\nNossa instituição acadêmica trabalha com sistema de Menções\nEsta nota corresponde a: ")

if nota >= 8:
    print("\nSS\n")
elif nota >= 6:
    print("\nMS\n")
elif nota >= 4:
    print("\nMM\n")
elif nota >= 2:
    print("\nMI\n")
else:
    print("\nII\n")