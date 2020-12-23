# This method reads the data from the file and returns the two players decks
def getInput(inputPath):
    fileP = open(inputPath, 'r')
    fileLines = fileP.readlines()
    fileP.close()

    player1Deck = []
    player2Deck = []

    secondPlayer = False
    firstPlayer = False
    for line in fileLines:
        line = line.strip()
        if line.find('Player') == 0:
            if firstPlayer == True:
                secondPlayer = True
                continue
            else:
                firstPlayer = True
                continue
            
        if line == '':
            continue

        if secondPlayer == True:
            player2Deck.append(int(line))
        else:
            player1Deck.append(int(line))

    return [player1Deck, player2Deck]

# This method simulats the games. If playRecursion is set to True, we would be
# playing recursive combat else a normal game. If subGame is set to True, that
# means we are in a subGame and there we need to do some things differently
def playGame(player1, player2, playRecursion=False, subGame=False):

    # get a copy of the initial player's decks. We do not want to overwrite them
    player1Deck = list(player1)
    player2Deck = list(player2)

    # The following will hold all the decks that a player has during various rounds
    # of the current game
    player1Hands = []
    player2Hands = []

    # We play the game until one of the players loses the game
    while 1:

        # If we have seen the current player deck from one of the player already
        # the first Player wins, else we add the current deck from both players to
        # the seen deck.
        ## We assume this check returns a winner only for a sub game, as the final
        ## winner has to have all the cards
        if player1Deck in player1Hands or player2Deck in player2Hands:
            return 'F'
        else:
            player1Hands.append(list(player1Deck))
            player2Hands.append(list(player2Deck))

        # Get the top card of the stack for both the players
        first = player1Deck.pop(0)
        second = player2Deck.pop(0)

        if playRecursion == True:
            # In recursion mode we need to play sub games if the current card value
            # for each player is less than the number of cards they have in their
            # decks
            if len(player1Deck) >= first and len(player2Deck) >= second:

                # Using recursion to play the sub games, the winner of the sub game
                # wins the current round
                winner = playGame(list(player1Deck[:first]), list(player2Deck[:second]), True, True)
                if winner =='F':
                    player1Deck += [first, second]
                else:
                    player2Deck += [second, first]
            else:
                # if no recursive game was played we follow the same rules, the player
                # with the higher card value wins the current round
                if first > second:
                    player1Deck += [first, second]
                else:
                    player2Deck += [second, first]
        else:
            # We are not in recursion, the player with the hgher card value wins the
            # current round
            if first > second:
                player1Deck += [first, second]
            else:
                player2Deck += [second, first]

        # the game ends when one of the players has no cards left
        if len(player2Deck) == 0 or len(player1Deck) == 0:
            break

    # If we are in a subgame we need to just let the main game know who is the winner
    # of this subgame. Using 'F' to denote first player won the subgame and 'S' for
    # second player
    if subGame == True:
        if len(player2Deck) == 0:
            return 'F'
        else:
            return 'S'
        
    # It comes here only when it is not a subGame as we return from above
    if len(player2Deck) == 0:
        winningDeck = player1Deck
    else:
        winningDeck = player2Deck

    # compute the winning player's score,using enumerate and len of winningDeck
    return sum([card * (len(winningDeck) - index) for index, card in enumerate(winningDeck)])

# Read the data into the palyers deck
[player1Deck, player2Deck] = getInput('D22.txt')

# Run the games for the two parts
print([playGame(player1Deck, player2Deck), playGame(player1Deck, player2Deck, True)])
