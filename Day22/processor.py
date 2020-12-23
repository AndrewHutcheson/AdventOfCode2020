stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

player1 = []
player2 = []
currentDeck = ""
for row in data:
    if row == "Player 1:":
        currentDeck = "player1"
    elif row == "Player 2:":
        currentDeck = "player2"
    elif(currentDeck == "player1"):
        player1.append(row)
    elif(currentDeck == "player2"):
        player2.append(row)

while (len(player1) > 0) and (len(player2) > 0):
    print("player 1's deck:",player1)
    print("player 2's deck:",player2)
    player1Card = player1.pop(len(player1)-1)
    player2Card = player2.pop(len(player2)-1)
    print("player1 plays:",player1Card)
    print("player2 plays:",player2Card)
    if player1Card > player2Card:
        print("player1 wins")
        player1.insert(0,player1Card)
        player1.insert(0,player2Card)
    else:
        print("player2 wins")
        player2.insert(0,player2Card)
        player2.insert(0,player1Card)
    print()

if(len(player1) > len(player2)):
    winner = player1
else:
    winner = player2

score = 0
index = 0
while index < len(winner):
    score += (index+1) * int(winner[index])
    print(index+1,"*",winner[index],"=",(index+1)*int(winner[index]))
    index += 1

print(score)