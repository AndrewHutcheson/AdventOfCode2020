#stream = open("input.txt")
stream = open("sampleInput.txt")
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
    #print("player 1's deck:",player1)
    #print("player 2's deck:",player2)
    player1Card = int(player1.pop(0))
    player2Card = int(player2.pop(0))
    #print("player1 plays:",player1Card)
    #print("player2 plays:",player2Card)
    if player1Card > player2Card:
        #print("player1 wins")
        player1.insert(len(player1),player1Card)
        player1.insert(len(player1),player2Card)
    else:
        #print("player2 wins")
        player2.insert(len(player2),player2Card)
        player2.insert(len(player2),player1Card)
    #print()

if(len(player1) > len(player2)):
    winner = player1
else:
    winner = player2

score = 0
index = 0
multiplier = len(winner)
while index < len(winner):
    score += multiplier * int(winner[index])
    #print(multiplier,"*",winner[index],"=",multiplier*int(winner[index]))
    index += 1
    multiplier -= 1
print("Part 1:",score)

##Part Two ##
#reset decks
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

previousConfigurations = []
#now I need a recursive function:
game = 1
def recursive_combat(player1,player2,theRound,game):
    theRound += 1
    inputGame = game
    if(player1 + player2) in previousConfigurations:
        player1 = player1 + player2
        player2 = []
        return [player1,player2,"Player1",game,theRound]

    else:
        print("Player 1's deck",player1)
        print("Player 2's deck",player2)
        player1Card = int(player1.pop(0))
        player2Card = int(player2.pop(0))
        print("Player 1 plays",player1Card)
        print("Player 2 plays",player2Card)
        if (len(player1) <= player1Card) and (len(player2) <= player2Card):
            print("playing subgame to determine winner...")
            results = recursive_combat(player1[0:player1Card],player2[0:player2Card],theRound,game+1)
            winner = results[2]
            if(winner == player1):
                player1.insert(len(player1),player1Card)
                player1.insert(len(player1),player2Card)
            else:
                player2.insert(len(player2),player2Card)
                player2.insert(len(player2),player1Card)
        else:
            if(player1Card > player2Card):
                winner = "Player1"
            else:
                winner = "Player2"
    if(winner == "Player1"):
        player1.insert(len(player1),player1Card)
        player1.insert(len(player1),player2Card)
    else:
        player2.insert(len(player2),player2Card)
        player2.insert(len(player2),player1Card)
    previousConfigurations.append((player1+player2))
    game = inputGame
    print(winner,"wins round",theRound,"of game",game)
    return [player1,player2,winner,game,theRound]

while (len(player1) > 0) and (len(player2) > 0):
    results = recursive_combat(player1,player2,1,game)
    #print("here",results[0])
    #print("here",results[1])
    player1 = results[0]
    player2 = results[1]
    winner = results[2]
    game = results[3]