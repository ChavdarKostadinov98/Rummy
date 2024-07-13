class Player:
    def __init__(self, name: str, country, cards: list = None):
        self.name = name
        self.country = country
        self.cards = cards if cards else []
        self.combos = []

    def __str__(self):
        return (f"{self.name}, {self.country}\n"
                f"Cards: {self.cards}\n"
                f"Combos: {self.combos}") if self.combos else f"{self.name}, {self.country}\nCards: {self.cards}\n"

    def receive_cards(self, card):
        self.cards.append(card)

    def take_from_pile(self, deck):
        self.receive_cards(deck.pile[-1])
        deck.remove_from_pile(deck.pile[-1])

    def take_from_deck(self, deck):
        self.receive_cards(deck.deck_of_cards[-1])
        deck.remove_card(deck.deck_of_cards[-1])

    def drop_combo(self, combo: list, deck):
        cards = [self.cards[card] for card in combo]
        deck.add_combo(cards)
        self.combos.append(cards)

    def add_to_combo(self, card: int, deck, combo: int):
        deck.combos[combo].append(self.cards[card])

    def throw_card(self, card: int, deck):
        deck.add_to_pile(self.cards[card])
        self.cards.remove(self.cards[card])

    def sort_hand(self):
        self.cards = sorted(self.cards, key=lambda card: (card.split()[2], self.rank_value(card.split()[0])))

    def rank_value(self, rank):
        if rank.isdigit():
            return int(rank)
        elif rank == "J":
            return 10
        elif rank == "Q":
            return 11
        elif rank == "K":
            return 12
        elif rank == "A":
            return 1





