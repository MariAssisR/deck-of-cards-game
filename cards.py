import json

# get raw data of cards and return only the value and the suit of each card
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

# find and return the winner with json
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