# student: CB018092 
# date: 2025/12/11
# topic: Iterative Control Structures

print("====================")
print("Welcome to the game")
print("====================")
totalPlayers = int(input("How many players:"))
multiple = int(input("Bus on which multiple:"))

# remainng player counter
playrCount = totalPlayers

# round counter
i = 1

#get of list of players
players = list(range(1, playrCount+1))

if(totalPlayers>=2):
    
    #main loop8
    while(playrCount>0):
        for player in range(totalPlayers):

            #find the player who won
            if(playrCount==1):
                for c in range(totalPlayers):
                    if players[c]!=0:
                        print("=============================")
                        print(f"Player {players[c]} Wins!")

                # Set main loop end
                playrCount = 0

            # break main loop
            if(playrCount==0):
                break

            #if player is out of game, proceed to next player
            if players[player]==0:
                continue 

            ans = input(f"player {players[player]} answer:")

            #set round answer
            round_ans = "bus"
            if(i%multiple!=0):
                round_ans=f"{i}"

            if(ans == round_ans):
                print("Correct !")

            else:
                print(f"Incorrect! Player {players[player]} lost!")

                # remove failed player from game
                players[player]=0 

                # set amount of players left in game
                playrCount = playrCount-1 

                # starts the round off where the last person failed, remove if unnecessary
                continue 

            # set next round
            i = i+1 
    print("Game Over!")
else:
    print("Need At least 2 players")
