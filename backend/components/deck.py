from random import shuffle


class Deck:
    def __init__(self):
        self.deck_of_cards = self.create_deck()
        shuffle(self.deck_of_cards)
        self.pile = []
        self.combos = []

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = [rank + " of " + suit for rank in ranks for suit in suits]
        return deck

    def __str__(self):
        if self.pile:
            return f"Card on top of pile: {self.pile[-1]}"

    def remove_card(self, card):
        self.deck_of_cards.remove(card)

    def add_to_pile(self, card):
        self.pile.append(card)

    def remove_from_pile(self, card):
        self.pile.remove(card)

    def add_combo(self, combo):
        self.combos.append(combo)

