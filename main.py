import requests
import json

# get a new deck and suffle it
def shuffleCardsAndGetDeck():
    shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

    try:
        response = requests.get(shuffle_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            # get the id of the deck
            data_deck_id =  data["deck_id"]
            return data_deck_id
        else:
            print(f"HTTP request error (Status code: {response.status_code})")
    except:
        print("HTTP request error in function shuffleCardsAndGetDeck\n")
        pass

# draw a count number of cards from deck_id
def dealCards(deck_id, count):
    draw_card_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    try:
        response = requests.get(draw_card_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            # get the count of cards of the deck with id equal deck_id
            data_cards = data["cards"]
            return data_cards
        else:
            print(f"HTTP request error (Status code: {response.status_code})")
    except:
        print("HTTP request error in function dealCards\n")
        pass

# get raw data of cards and return only the value and the suit of it
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

        cards.append({"value": value,"suit": mapping_suit[suit]})

    return cards

# order the cards in order of: first=suit and second=value
def orderCards(card):
    order_suit = {"paus": 0, "ouros": 1, "copas": 2, "espadas": 3}
    return (order_suit[card["suit"]], int(card["value"]))

# return if a hand of ordered cards has a sequence
# sequence = 3 or more consecutive cards 
def checkForSequence(cards):
    for index in range(len(cards) - 2):
        card1 = cards[index]
        card2 = cards[index + 1]
        card3 = cards[index + 2]

        if(card1["suit"] == card2["suit"] == card3["suit"]):
            if(int(card1["value"]) == int(card2["value"])-1 == int(card3["value"])-2):
                return True
    return False

# prepare cards in list to output
def outputCards(cards):
    output_cards = []
    for card in cards:
        output_cards.append(str(card["value"])+" de "+card["suit"])
    return output_cards

def findWinner(alan_cards, bruno_cards):
    result = {}
    alan_sequence = checkForSequence(alan_cards)
    result["alan"] = {
        "cartas": outputCards(alan_cards),
        "tem_sequencia": alan_sequence
    }
    bruno_sequence = checkForSequence(bruno_cards)
    result["bruno"] = {
        "cartas": outputCards(bruno_cards),
        "tem_sequencia": bruno_sequence
    }

    if(alan_sequence and not bruno_sequence):
       result["vencedor"] = "alan"
    elif(bruno_sequence and not alan_sequence):
        result["vencedor"] = "bruno"
    else:
        result["vencedor"] = "empate"

    return result

############################################################

# MAIN
# start game
# shuffle, deal cards, order cards, check for sequence, output
# play again?

# get new deck and suffle
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






