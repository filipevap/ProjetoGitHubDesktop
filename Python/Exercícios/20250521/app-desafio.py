"""Criem um jogo chamado A Ilha dos Códigos Perdidos.

O jogo precisa ter:

Nome do jogador;
Idade;
Vida inicial de 100;
Energia inicial de 50;
Pelo menos 5 fases;
Escolhas com if/elif/else;
Pelo menos 1 while;
Pelo menos 1 for;
Uso de operadores matemáticos;
Uso de operadores relacionais;
Uso de and, or ou not;
final de vitória ou derrota."""

#A Ilha dos Códigos Perdidos

#FASE 1 - chegou na ilha
vida = 100;
energia = 50;

print("=====================\nVocê chegou na ilha\n=====================")
print(f"Energia: {energia}\nVida: {vida}\n\n")
fase1 = int(input("Você encontrou na praia uma cabana e um barco abandonado.\nMas a chuva está chegando e você só tem tempo para correr para um dos dois lugares.\nPra onde você vai?\n\nCabana = 1 ou Barco=2"))



#cabana ou barco
#FASE 2 CABANA 1
print("=====================\nFASE 2\n=====================")

if fase1 == 1:
    energia -= 10
    vida = 100
    print(f"Energia: {energia}\nVida: {vida}")
    
    fase2 = int(input("Caraca.. Você se deparou com um variável virulenta totalmente virulosa e que acabou te virulando e você acabou descobrindo que deve ir para o barco. Digite '2'"))

#FASE 2 BARCO 2
else:
    print("=====================\nFASE 2\n=====================")
    energia -= 10
    vida = 100
    print(f"Energia: {energia}\nVida: {vida}")
    fase2 = int(input("Ao chegar no barco você encontrou uma faca e um espelho. Contudo, pode escolher apenas um dos itens pois está com os bolsos cheios. Escolha apenas 1\nFaca - 3            Espelho - 4"))




#FASE 3 - faca e espelho
if fase2 == 2: #ESCOLHA FACA
    print("=====================\nFASE 2\n=====================")
    energia -= 10
    vida = 100
    print(f"Energia: {energia}\nVida: {vida}")

    fase3 = int(input("Ao chegar no barco você encontrou uma faca e um espelho. Contudo, pode escolher apenas um dos itens pois está com os bolsos cheios. Escolha apenas 1\nFaca - 3            Espelho - 4"))

elif fase3 == 3:
    print("=====================\nFASE 2\n=====================")
    energia -= 10
    vida = 100
    print(f"Energia: {energia}\nVida: {vida}")
  
    print("meu deus, que desastrado!!! Você acabou tropeçando na tábua do barco e caiu sobre a faca... Perca 50 de Energia")

else:
    print("escolheu o espelho")
#FASE 4

energia -= 10


#FASE 5

energia -= 10
