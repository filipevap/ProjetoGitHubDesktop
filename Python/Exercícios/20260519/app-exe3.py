'''03 Senha simples
crie uma fixa: 1234.
Peça para o usuário digitar uma senha.
Se estiver corret, mostre "acesso permitido" Senão Senha incorreta.'''

senha = int(input("Escolha sua senha de 4 dígitos: "))
print("\nMuito bem, você escolheu a sua senha.\nAgora, para dar prosseguimento ao processo e ter acesso às informações secretas, apresente sua senha:")

conferesenha = int(input("\nDigite novamente sua senha de quatro dígitos: \n"))

if conferesenha == senha:
    print(f"\nSENHA CORRETA.\n\n\nPrepare-se para a maior revelação da sua vida")
else:
    print("\nVocê morrer sem ficar sabendo")