'''01 Número positivo ou negativo
Peça um número.
Se for mairo que zero, mostre "Número positivo."
Senão, mostre "Número negativo ou zero".'''

nome = input("Qual é mesmo seu nome? ")
valor = float(input(f"Não quero te roubar, {nome}, eu juro! Mas quanto você tem na sua conta bancária? "))

if valor > 0:
    print(f"Uiuiuuuui, riquinho. Você tem R$ {valor:.2f}")
elif valor == 0:
    print(f"{nome}, você tá quebrado, hein?! kkkk")
else:
    print(f"{nome}, me dá seu endereço pra eu te mandar uma cesta básica.")