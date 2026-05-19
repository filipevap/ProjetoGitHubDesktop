'''03 Senha simples
crie uma fixa: 1234.
Peça para o usuário digitar uma senha.
Se estiver corret, mostre "acesso permitido" Senão Senha incorreta.'''

senha = int(input("Escolha sua senha de 4 dígitos:\n"))
conferesenha = int(input("\nMuito bem, você escolheu a sua senha.\nAgora, para dar prosseguimento ao processo e ter acesso às informações secretas,\napresente sua senha:\n"))

while conferesenha != senha:
    print("\nSENHA INCORRETA.\n\n\nDigite novamente a sua senha: ")
    conferesenha = senha
else:
    print("\nDescubra o segredo: O número 1234 é a senha mais utilizada no mundo, e é a senha mais fácil de ser descoberta por hackers. Portanto, não utilize esta senha para proteger suas informações pessoais, pois elas podem ser facilmente acessadas por pessoas mal-intencionadas.")