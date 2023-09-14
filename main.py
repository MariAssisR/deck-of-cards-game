import json
from api import shuffleCardsAndGetDeck, dealCards
from cards import arrangeCardsFromApi, orderCards, checkForSequence, outputCards, findWinner

# MAIN
# start game
# shuffle, deal cards, order cards, check for sequence, output
def startGame():
    # get new deck and suffle it
    deck_id = shuffleCardsAndGetDeck()

    # get alan cards
    alan_unarranged_cards = dealCards(deck_id,11)
    alan_unordered_cards = arrangeCardsFromApi(alan_unarranged_cards)
    alan_cards = sorted(alan_unordered_cards, key=orderCards)

    # get bruno cards
    bruno_unarranged_cards = dealCards(deck_id,11)
    bruno_unordered_cards = arrangeCardsFromApi(bruno_unarranged_cards)
    bruno_cards = sorted(bruno_unordered_cards, key=orderCards)

    # find and print winner
    output = findWinner(alan_cards, bruno_cards)
    output_json = json.dumps(output, indent=4)
    print(output_json)


if __name__ == "__main__":
    startGame()