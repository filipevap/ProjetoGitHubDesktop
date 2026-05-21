#Crie um programa que faça o cadastro de uma compra.
#O programa deve pedir:
#Nome do cliente
#Idade do cliente
#Valor da compra
#Se o cliente pagou o boleto: sim ou não
#Se o cliente é cliente VIP: sim ou não
#Depois, o programa deve mostrar:
#nome do cliente;
#idade;
#valor da compra;
#se o boleto foi pago;
#se o cliente é VIP;
#mensagem final dizendo se a compra foi liberada ou ficou pendente.'''

nome = input("Qual o seu nome?\n")
idade = int(input("\nQual a sua idade?\n"))
compra = float(input("\nQual o valor da sua compra?\n"))
pgboleto = input("\nVocê pagou o boleto? Digite Sim ou Não\n")
vip = input("\nVocê está inscrito no nosso programa de clientes VIP? Informe Sim ou Não\n")

pgboleto = pgboleto.lower()
if pgboleto == "sim":
    pgboleto = "O cliente pagou o boleto"
else:
    pgboleto = "O cliente não pagou o boleto"

vip = vip.lower()
if vip == "sim":
    vip = "O cliente é top das galáxias. Está no grupo VIP"
else:
    vip = "O cliente é pé de boi. Não precisa dar moral porque não é VIP"

aprovacao = "a"
if pgboleto == "O cliente pagou o boleto" and vip == "O cliente é top das galáxias. Está no grupo VIP":
    aprovacao = "O cliente está aprovadíssimo! Volte sempre"
elif pgboleto == "O cliente pagou o boleto" and vip != "O cliente é top das galáxias. Está no grupo VIP":
    aprovacao = "Sua compra está aprovada! Aproveite para aderir ao nosso grupo de clientes VIP's"
else:
    aprovacao = "Infelizmente, sua compra não foi aprovada.\nRealize o pagamento do boleto.\n\nAproveite para aderir ao nosso clube VIP para ter ainda mais descontos"

print(f"""|Nome: {nome}|\n\nIdade: {idade}\n\nValor da compra: R$ {compra:.2f}\n\nSituação do boleto: {pgboleto}\n\nClube VIP: {vip}\n\nSituação da compra: {aprovacao}""")
