# date: 2025/12/11
# topic: Iterative Control Structures

def doRound(player,round,multiple):
    """
    This is a function to check round answer against player answer

    Args:
        player: current round player
        round: the round the game is currently on 
        multiple: the multiple the bus value is checked upon

    returns:
        int: 1 - correct | 0 - incorrect | -1 - invalid 
    """
    try:
        ans = input(f"player {player} answer:")

        if(ans != 'bus'):
            try:
                int(ans)
            except ValueError as e:
                raise(ValueError)
        
        #set round answer
        round_ans = "bus" if (round % multiple == 0) else str(round)
        
        if(ans == round_ans):
            return 1
        else:
            return 0;

    except ValueError as e:
        print("Error:","Please Enter round asnwer correctly\n('bus' or value as integer)")

    return -1

def getGameData():
    """
    This is a function to get game data from the player

    Args:
        none

    Returns:
        values:both values as a list or -1 if error
    """
    try:
        totalPlayers = int(input("How many players:"))
        multiple = int(input("Bus on which multiple:"))

        if(totalPlayers<2):
            print("At least 2 players are needed")
        elif(multiple<2):
            print("At least a multiplier of 2 is required")
        else:
            return [totalPlayers,multiple]
    
    except ValueError as e:
        print("Error:","Please correctly enter values for the game data")
    
    return -1

def main():
    print("====================")
    print("Welcome to the game")
    print("====================")
    
    # number of player, the multiple
    gameData = getGameData()

    if(gameData!=-1):
        # round counter
        i = 1

        #get of list of players
        players = list(range(1, gameData[0]+1))

        #main loop
        while(len(players)>0):
            #find the player who won
            if(len(players)==1):
                print("=============================")
                print(f"Player {players[0]} Wins!")
                break

            player = players[(i//len(players)) // gameData[0]]

            #if player is out of game, proceed to next player
            if player not in players:
                continue 

            round_ans = doRound(player,i,gameData[1])

            if(round_ans == 1):
                print("Correct!")
            elif(round_ans == 0):
                print(f"Incorrect! Player {player} lost!")

                # remove failed player from game
                del players[players.index(player)]

                # starts the round off where the last person failed, remove if unnecessary
                continue 
            else:
                # starts the round off where the last person failed, remove if unnecessary
                continue 

            # set next round
            i = i+1 

        print("Game Over!")


if __name__ == "__main__":
    main()