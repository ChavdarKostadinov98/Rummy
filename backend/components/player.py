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

    def drop_combo(self, combo_index: int, deck):
        combo = self.combos.pop(combo_index)
        for card in combo:
            self.cards.remove(card)
        deck.add_combo(combo)

    def add_to_combo(self, card_index: int, deck, combo_index: int):
        card = self.cards.pop(card_index)
        deck.combos[combo_index].append(card)

    def throw_card(self, card_index: int, deck):
        deck.add_to_pile(self.cards[card_index])
        self.cards.remove(self.cards[card_index])

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

    def detect_sets(self):
        rank_count = {}
        sets = []

        for card in self.cards:
            rank = card.split()[0]
            if rank in rank_count:
                rank_count[rank] += 1
            else:
                rank_count[rank] = 1

        for rank, count in rank_count.items():
            if count >= 3:
                set_cards = [card for card in self.cards if card.split()[0] == rank]
                sets.append(set_cards)

        return sets

    def detect_sequences(self):
        suits = self.group_by_suits()
        sequences = []
        rank_values, reverse_rank_values = self.get_rank_mappings()

        for suit in suits:
            suits[suit].sort()

        for suit, ranks in suits.items():
            sequences.extend(self.find_sequences(ranks, suit, reverse_rank_values))

        return sequences

    def group_by_suits(self):
        suits = {"Hearts": [], "Diamonds": [], "Spades": [], "Clubs": []}
        rank_values, _ = self.get_rank_mappings()

        for card in self.cards:
            rank, _, suit = card.split()
            suits[suit].append(rank_values[rank])

        return suits

    def get_rank_mappings(self):
        rank_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
        reverse_rank_values = {v: k for k, v in rank_values.items()}
        return rank_values, reverse_rank_values

    def find_sequences(self, ranks, suit, reverse_rank_values):
        sequences = []
        sequence = []

        for i in range(len(ranks)):
            if i == 0 or ranks[i] == ranks[i - 1] + 1:
                sequence.append(ranks[i])
            else:
                if len(sequence) >= 3:
                    sequences.append([reverse_rank_values[rank] + " of " + suit for rank in sequence])
                sequence = [ranks[i]]

        if len(sequence) >= 3:
            sequences.append([reverse_rank_values[rank] + " of " + suit for rank in sequence])

        return sequences

    def detect_combos(self):
        self.combos = self.detect_sets() + self.detect_sequences()
        return self.combos

    def display_combos(self):
        print(f"Combos for {self.name}:")
        for combo in self.combos:
            print(combo)

    def display_hand(self):
        print(f"{self.name}'s hand: {', '.join(self.cards)}")
