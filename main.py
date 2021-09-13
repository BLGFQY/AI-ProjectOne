import random


def evaluation(hand):

    # variable to hold number of each suit in a hand
    #   Clubs, Spades, Diamonds, Hearts
    distr = [0, 0, 0, 0]

    score = 0

    print("hand = ", hand)
    print("hand slice = ", hand[3:])
    for i in range(1, 14):
        # score primary player hand
        if hand[i][0] == 1: score += 4
        if hand[i][0] == 13: score += 3
        if hand[i][0] == 12: score += 2
        if hand[i][0] == 11: score += 1

        # count number of each suit
        if hand[i][1] == "Clubs": distr[0] += 1
        if hand[i][1] == "Spades": distr[1] += 1
        if hand[i][1] == "Diamonds": distr[2] += 1
        if hand[i][1] == "Hearts": distr[3] += 1

    # score number of suits
    size = len(distr)
    for k in range(size):
        if distr[k] == 0: score += 5
        if distr[k] == 1: score += 2
        if distr[k] == 2: score += 1

    return score

print("Cards appear as follows:\n   1(Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, 11(Jack), 12(Queen), 13(King)\n")

totalHands = 1000
play = True

while play:
    # Build Deck
    # this loop puts the deck together
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    deck = []
    for i in suits:
        for j in range(1, 14):
            deck.append([j, i])
    random.shuffle(deck)

    # primary player hand variables
    primary = [] # hold cards in hand
    score = 0

    primary.append(deck[:13])
    deck = deck[13:]

    score = evaluation(primary)
    # variable to hold number of each suit in a hand
    #   Clubs, Spades, Diamonds, Hearts
    # distr = [0, 0, 0, 0]
    #
    # # PRIMARY PLAYER
    # for i in range(1, 14):
    #
    #     # create primary player hand
    #     primary.append(deck[i])
    #
    #     # score primary player hand
    #     if deck[i][0] == 1 : score += 4
    #     if deck[i][0] == 13 : score += 3
    #     if deck[i][0] == 12 : score += 2
    #     if deck[i][0] == 11 : score += 1
    #
    #     # count number of each suit
    #     if deck[i][1] == "Clubs" : distr[0] += 1
    #     if deck[i][1] == "Spades" : distr[1] += 1
    #     if deck[i][1] == "Diamonds" : distr[2] += 1
    #     if deck[i][1] == "Hearts" : distr[3] += 1
    #
    #     # remove primary player hand from deck
    #     deck.remove(deck[i])
    #
    # # score number of suits
    # size = len(distr)
    # for k in range(size):
    #     if distr[k] == 0: score += 5
    #     if distr[k] == 1: score += 2
    #     if distr[k] == 2: score += 1


    print("Here is your hand\n", primary)
    print("This hand is worth", score, " points.")
    print("Running simulation.....")
    #################################################

    # secondary player hand variables
    secondary = [] # holds card in hand
    secondaryScore = 0

    # variable to calculate results
    # Pass, Part Score, Game, Small Slam, Grand Slam
    outcome = [0, 0, 0, 0, 0]

    # SECONDARY PLAYER
    for i in range(0, totalHands):

        #reset variables
        distr = [0, 0, 0, 0]
        secondaryScore = 0
        secondary.clear()

        # loop deals one hand
        for j in range(1, 14):
            random.shuffle(deck)
            secondary.append(deck[j])

            # score partner hand
            if deck[j][0] == 1 : secondaryScore += 4
            if deck[j][0] == 13 : secondaryScore += 3
            if deck[j][0] == 12 : secondaryScore += 2
            if deck[j][0] == 11 : secondaryScore += 1

            # count number of suits in partner hand
            if deck[j][1] == "Clubs" : distr[0] += 1
            if deck[j][1] == "Spades" : distr[1] += 1
            if deck[j][1] == "Diamonds" : distr[2] += 1
            if deck[j][1] == "Hearts" : distr[3] += 1

        # score suits for partner
        size = len(distr)
        for k in range(size):
            if distr[k] == 0: secondaryScore += 5
            if distr[k] == 1: secondaryScore += 2
            if distr[k] == 2: secondaryScore += 1

        #RESULTS
        #print(i, "  P.Score = ", partnerScore, "  T.Score = ", partnerScore + score)
        total = score + secondaryScore
        if (total < 20) : outcome[0] += 1
        if (19 < total < 26) : outcome[1] += 1
        if (25 < total < 32) : outcome[2] += 1
        if (31 < total < 36) : outcome[3] += 1
        if (total > 35) : outcome[4] += 1

    # loop coverts from raw data to percent chance
    size = len(outcome)
    for i in range(size):
        outcome[i] = (outcome[i]/totalHands) * 100

    print("\nThe estimated probability based on", totalHands ,"simulated hands:")
    print("Pass: ", outcome[0], '%')
    print("Part Score: ", outcome[1], '%')
    print("Game: ", outcome[2], '%')
    print("Small Slam: ", outcome[3], '%')
    print("Grand Slam: ", outcome[4], '%')

    play = input("Would you like to play another hands? (true/false) ")


