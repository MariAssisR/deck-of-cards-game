import requests
import json

# get a new deck, suffle it and return its ID
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

# draw a count number of cards from deck with specified ID
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