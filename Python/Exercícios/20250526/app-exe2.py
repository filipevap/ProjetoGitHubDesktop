'''2 - Solicite ao usuário 1 número e informe se este é par ou
ímpar.'''

num = int(input("Digite um número e lhe direi se ele é par ou ímpar:\n\n"))

if num % 2 == 0:
    print("\nO número é par\n")
else:
    print("\nO número é ímpar\n")