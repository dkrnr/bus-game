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
        ans = input(f"Player {player} answer:").lower()

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
            # print("Round Ans:",round_ans)
            return 0

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
        print()

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
    print("=========")
    print("Bus Game")
    print("=========")
    print()
    
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
                print("================")
                print(f"Player {players[0]} Wins!")
                break
            
            player_index = (i%(gameData[0]))-1

            round_ans = doRound(players[player_index],i,gameData[1])

            if(round_ans == 1):
                print("Correct!")
                print()
            elif(round_ans == 0):
                print(f"Incorrect! Player {players[player_index]} lost!")
            
                # remove failed player from game
                del players[player_index]

                # display remaining players (skips if 1 player becoz the game will end next round)
                if(len(players)>1):
                    print("\nRemaining players")
                    for ply in players:
                        print(f"> Player {ply}")
                          
                print()
                
                # starts the round off where the last person failed, remove if unnecessary
                continue 
            else:
                # starts the round off where the last person failed, remove if unnecessary
                continue 

            # set next round
            i += 1 

        print("Game Over!")


if __name__ == "__main__":
    main()