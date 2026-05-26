'''Python – Exercício Fixação

● Crie algoritmos que:
1 - Solicite ao usuário dois números inteiros. O programa

deve comparar os dois valores e exibir qual deles é o maior.'''

num1 = int(input("Digite um número:\n"))
num2 = int(input("Digite outro número:\n"))

if num1 > num2:
    print(f"O número {num1} é maior que {num2}")

elif num1 < num2:
    print(f"O número {num2} é maior que {num1}")
else:
    print("Os números são iguais")
