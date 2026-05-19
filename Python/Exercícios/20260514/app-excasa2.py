#Compras na loja
#uma pessoa foi a loja e comprou vários produtos.
#Faça um programa que pergunte ao usuário o valor de cada item a baixo
#camiseta, calça, tenis, bone, mochila e cinto.
#Dpois o program deve:
#Calcular o valor total da compra, mostrar quanto ficaria se a pessoa ganhasse 30 reais de desconto, mostrar quanto ficaria se a pessoa resolvesse comprar mais uma camiseta e no final mostrar todos os resultados na tela


camiseta = float(input("Qual o valor da camiseta? "))
calca = float(input("Qual o valor da calça? "))
tenis = float(input("Qual o valor do tênis? "))
bone = float(input("Qual o valor do boné? "))
mochila = float(input("Qual o valor da mochila? "))
cinto = float(input("Qual o valor do cinto? "))
total = camiseta+calca+tenis+bone+mochila+cinto
print(f"A sua compra custou R$ {total:.2f}. Se for pagar no PIX eu vou te dar R$ 30,00 de desconto: vai ficar R$ {total-30:.2f}. Se for levar mais uma camiseta, ficará {total+camiseta-30:.2f}, já com desconto")