from backend.components.player import Player
from backend.components.deck import Deck
from backend.app.game import Game
from backend.app.engine import Engine
from backend.components.dealer import Dealer


if __name__ == "__main__":
    deck = Deck()
    players = [Player("Alice", "USA"), Player("Bob", "Canada")]
    dealer = Dealer(deck)
    game = Game(deck, dealer, players)
    engine = Engine(game)

    engine.start_game()
