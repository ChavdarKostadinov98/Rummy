from backend.components.player import Player
from backend.components.deck import Deck
from typing import List


class Dealer:
    def __init__(self, deck: Deck):
        self.cards = deck

    def deal_cards(self, deck, players: List[Player]):
        cards_per_player = 9

        for _ in range(cards_per_player):
            for each_player in players:
                each_player.receive_cards(deck.deck_of_cards[-1])
                deck.remove_card(deck.deck_of_cards[-1])

        deck.add_to_pile(deck.deck_of_cards[-1])
        deck.remove_card(deck.deck_of_cards[-1])
