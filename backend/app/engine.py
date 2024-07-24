from backend.app.game import Game
from backend.components.player import Player


class Engine:
    def __init__(self, game: Game):
        self.game = game

    def take_turn(self, player: Player):
        print(f"\n{player.name}'s turn:")
        player.detect_combos()
        player.display_combos()
        player.sort_hand()
        player.display_hand()
        print(f"Top card on pile: {self.game.deck.pile[-1] if self.game.deck.pile else 'None'}\n")

        action_taken = False

        while not action_taken:
            command = input(f"{player.name}, enter your command: ").strip().lower()

            if command == "take from pile":
                player.take_from_pile(self.game.deck)
                print(f"{player.name} took {player.cards[-1]} from the pile.\n")
                action_taken = True
            elif command == "take from deck":
                player.take_from_deck(self.game.deck)
                print(f"{player.name} took {player.cards[-1]} from the deck.\n")
                action_taken = True

        player.sort_hand()
        player.display_hand()
        player.detect_combos()
        player.display_combos()

        while True:
            command = input(f"{player.name}, enter your command to drop combos or throw a card: ").strip().lower()

            if command.startswith("drop combo"):
                try:
                    combo_index = int(command.split()[2])
                    if 0 <= combo_index < len(player.combos):
                        player.drop_combo(combo_index, self.game.deck)
                        print(f"{player.name} dropped a combo.\n")
                        player.display_combos()
                        player.display_hand()
                    else:
                        print("Invalid combo index.")
                except ValueError:
                    print("Invalid command format. Use 'drop combo {combo_index}'")
            elif command.startswith("throw card"):
                try:
                    card_index = int(command.split()[2])
                    if 0 <= card_index < len(player.cards):
                        player.throw_card(card_index, self.game.deck)
                        print(f"{player.name} threw a card.\n")
                        break
                    else:
                        print("Invalid card index.")
                except ValueError:
                    print("Invalid command format. Use 'throw card {card_index}'")
            else:
                print("Invalid command. Try again.")

    def start_game(self):
        self.game.dealer.deal_cards(self.game.deck, self.game.players)
        self.game.current_player = self.game.players[0]

        while True:
            self.take_turn(self.game.current_player)
            current_index = self.game.players.index(self.game.current_player)
            self.game.current_player = self.game.players[(current_index + 1) % len(self.game.players)]
