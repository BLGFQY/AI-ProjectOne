import random


def evaluation(hand):

    # variable to hold number of each suit in a hand
    #   Clubs, Spades, Diamonds, Hearts
    distr = [0, 0, 0, 0]

    score = 0

    # score player hand
    for i in range(0, 13):
        # adds points to the players score for Jacks, Queens, Kings, and Aces
        if hand[i][0] > 10: score += (hand[i][0] % 10)

        # count number of each suit
        if hand[i][1] == "Clubs": distr[0] += 1
        if hand[i][1] == "Spades": distr[1] += 1
        if hand[i][1] == "Diamonds": distr[2] += 1
        if hand[i][1] == "Hearts": distr[3] += 1

    # score distribution of suits
    size = len(distr)
    for k in range(size):
        if distr[k] == 0: score += 5
        if distr[k] == 1: score += 2
        if distr[k] == 2: score += 1

    return score


print("\nCards appear as follows:\n    2, 3, 4, 5, 6, 7, 8, 9, 10, 11(Jack), 12(Queen), 13(King), 14(Ace)")
# Jack (11) (+1) | Queen (12) (+2) | King (13) (+3) | Ace (14) (+4) | doubleton (+1) | singleton (+2) | void (+5)

totalHands = 1000
play = True

while play:
    # this loop builds the deck in the form of a 2d list
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    deck = []
    for i in suits:
        for j in range(2, 15):
            deck.append([j, i])
    random.shuffle(deck)

    # player is dealt a hand and it's scored
    primary = deck[:13] # hold cards in hand
    deck = deck[13:]    # deletes primary hand from deck
    score = evaluation(primary)

    print("\nHere is your hand\n", primary)
    print("This hand is worth", score, " points.")
    print("Running simulation.....")

    # variable to calculate results
    # Pass, Part Score, Game, Small Slam, Grand Slam
    outcome = [0, 0, 0, 0, 0]

    # SECONDARY PLAYER
    for i in range(0, totalHands):
        # creates partner hand and evaluates
        random.shuffle(deck)
        secondary = deck[:13]
        secondaryScore = evaluation(secondary)

        #RESULTS
        total = score + secondaryScore
        if (total < 20) : outcome[0] += 1
        if (19 < total < 26) : outcome[1] += 1
        if (25 < total < 32) : outcome[2] += 1
        if (31 < total < 36) : outcome[3] += 1
        if (total > 35) : outcome[4] += 1

    # loop coverts from raw data to percent chance
    size = len(outcome)
    for i in range(size): outcome[i] = (outcome[i]/totalHands) * 100

    print("\nThe estimated probability based on", totalHands ,"simulated hands:")
    print("Pass: ", outcome[0], '%')
    print("Part Score: ", outcome[1], '%')
    print("Game: ", outcome[2], '%')
    print("Small Slam: ", outcome[3], '%')
    print("Grand Slam: ", outcome[4], '%')

    play = input("\nWould you like to play another hands? (true/false) ")


