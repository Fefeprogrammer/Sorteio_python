import random

frutas = ["banana", "manga", "maça", "melancia", "jaboticaba", "laranja"]

if "goiaba" in frutas:
    print("Sim. Tem manga na lista")
else:
    print("Não. Não tem manga na lista")


print("As frutas disponiveis são:")
for x in frutas:
    print(x)

rand = random.randrange(0, 6)

if(rand == 0):
    print("Voce ganhou uma banana")
elif(rand == 1):
    print("Voce ganhou uma manga")
elif(rand == 2):
    print("Voce ganhou uma maça")
elif(rand == 3):
    print("Voce ganhou uma melancia")
elif(rand == 4):
    print("Voce ganhou uma jaboticaba")
elif(rand == 5):
    print("Voce ganhou uma laranja")
