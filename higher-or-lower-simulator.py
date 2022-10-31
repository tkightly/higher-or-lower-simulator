from logging import critical
import math, time, sys, argparse
from sre_constants import SUCCESS
import matplotlib.pyplot as plt
import itertools

import random

def main(cards, threshold):

    # Build list of cards
    cardsList = list(range(2,15))*4
    
    # Shuffle them
    random.shuffle(cardsList)

    # Draw a card
    for currentCard in range(0,cards):
        print("Current card is ", cardsList[currentCard])

        # Save the current card
        currentCard = cardsList[currentCard]

        cardsList.remove(currentCard)

        print("There are %s cards remaining" % (len(cardsList)))

        # Work out how many cards are in the deck that are equal to or higher than the current card
        numHigherCards = 0
        for card in cardsList:
            #print("--card is ", card)
            if card >= currentCard:
                #print("---Card %s is higher than or equal to %s" % (card, currentCard))
                numHigherCards += 1

        # Work out odds
        currentHigherOdds = (numHigherCards/len(cardsList))*100
        currentLowerOdds = 100-currentHigherOdds

        print("There are %s cards with a value higher than %s" % (numHigherCards, currentCard))

        print("Odds of next card being higher than or equal to current card: ", currentHigherOdds)
        print("Odds of next card being lower than current card: ", currentLowerOdds)


    # do until --cards is reached
        #Draw the card, work out the odds based on cards remaining
   
    # Output the bar chart
    """
    plt.bar(reportOutcome, reportProbability)
    plt.title('Probablity')
    plt.xlabel('Outcome')
    plt.ylabel('Probability')
    plt.show()
    """

if __name__ == '__main__':
    
    # parse parameters from command line
    parser=argparse.ArgumentParser()

    # configure command line parameters
    parser.add_argument("--cards", help="How many cards")
    parser.add_argument("--threshold", help="The number at which you'll always say higher")
    args=parser.parse_args()

    #main(args.sides, args.quantity)
    main(2, 8)
    
