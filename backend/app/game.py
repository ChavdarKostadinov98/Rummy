from backend.components.dealer import Deck, Dealer
from backend.components.player import Player
from typing import List


class Game:
    def __init__(self, deck_for_game: Deck, dealer_for_game: Dealer, players_for_game: List[Player]):
        self.deck = deck_for_game
        self.dealer = dealer_for_game
        self.players = players_for_game
        self.current_player: Player





