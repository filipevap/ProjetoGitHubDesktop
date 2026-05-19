'''01 Maior de idade
Peça a idade da pessoa.
Se ela tiver 18 nos ou mais, mostre
"Você é maior de idade".
Senão, mostre "Você é menor de idade".'''

nome = input("Qual o seu nome? ")

idade = int(input(f"{nome}, você não passa de um delinquente! Eu sou uma autoridade policial! Quantos anos você tem?"))

if idade >= 18:
    print("Você já responde pelos seus atos. Já para o corró!")
else:
    print("Apanhou pouco em casa, hein?! Liguem para os pais deste garoto, pois ele não responde por si próprio")
 
