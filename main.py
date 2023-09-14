import requests
import json

# AUX
def shuffleCardsAndGetDeck():
    shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

    try:
        response = requests.get(shuffle_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            #get the id of the deck
            data_deck_id =  data["deck_id"]
            return data_deck_id
        else:
            print(f"HTTP request error (Status code: {response.status_code})")
    except:
        print("HTTP request error in function shuffleCardsAndGetDeck\n")
        pass
        
def dealCards(deck_id, count):
    draw_card_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    try:
        response = requests.get(draw_card_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            #get the count of cards of the deck with id equal deck_id
            data_cards = data["cards"]
            return data_cards
        else:
            print(f"HTTP request error (Status code: {response.status_code})")
    except:
        print("HTTP request error in function dealCards\n")
        pass

def arrangeCardsFromApi(raw_cards_data):
    mapping_value = {
        "ACE": 1,
        "JACK": 11,
        "QUEEN": 12,
        "KING": 13
    }
    mapping_suit = {
        "CLUBS": "paus",
        "HEARTS": "copas",
        "SPADES": "espadas",
        "DIAMONDS": "ouros"
    }

    cards = []
    for raw_card in raw_cards_data:
        value = raw_card["value"]
        suit = raw_card["suit"]

        if value in mapping_value:
            value = mapping_value[value]

        if suit in mapping_suit:
            suit = mapping_suit[suit]

        cards.append({"value": value,"suit": suit})

    return cards

def orderCards():
    pass

def checkForSequence():
    pass

def findWinner():
    pass

############################################################
deck_id = shuffleCardsAndGetDeck()
alan_unarranged_cards = dealCards(deck_id,10)
print(alan_unarranged_cards)
alan_cards = arrangeCardsFromApi(alan_unarranged_cards)
print(alan_cards)
for card in alan_cards:
    print(card["value"])
    print("\n")

# MAIN
# start game
# shuffle, deal cards, order cards, check for sequence, output
# play again?


