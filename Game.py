from Card import Card

class Game:
    """
    A class to represent a game with different card arrays: deck, basement, red_room, and blue_room.
    """

    def __init__(self):
        """
        Initialize the Game with empty card arrays.
        """
        self.deck = []
        self.basement = []
        self.red_room = []
        self.blue_room = []
        # Characters
        self.characters = []
        # Bad guys
        # No 1
        mouse = Card(1, "Mouse", "None", "None", "deck", False)
        self.characters.append(mouse)
        
        # No 2
        frog = Card(2, "Frog", "None", "None", "deck", False)
        self.characters.append(frog)
        
        # No 3
        josh = Card(3, "Joshua", "None", "None", "deck", False)
        self.characters.append(josh)

        # No 4
        travis = Card(4, "N4", "None", "None", "deck", False)
        self.characters.append(travis)

        # No 5
        cindi = Card(5, "Cindirella", "None", "None", "deck", False)
        self.characters.append(cindi)

        # No 6
        harman = Card(6, "Harman", "None", "None", "deck", False)
        self.characters.append(harman)

        # No 7
        chick = Card(7, "Some_chick", "None", "None", "deck", False)
        self.characters.append(chick)
        
        # No 8
        bad_boy = Card(8, "Lance", "None", "None", "deck", False)
        self.characters.append(bad_boy)
        
        # Good guys
        # No 11
        boyfriend = Card(11, "boyfriend", "None", "None", "deck", True)
        self.characters.append(boyfriend)

        # No 12
        bond = Card(12, "bond", "None", "None", "deck", True)
        self.characters.append(bond)

        # No 13
        girlfriend = Card(13, "girlfriend", "None", "None", "deck", True)
        self.characters.append(girlfriend)

        # No 14
        nathan = Card(14, "Nathan", "None", "None", "deck", True)
        self.characters.append(nathan)

        # No 15
        nina = Card(15, "Nina", "None", "None", "deck", True)
        self.characters.append(nina)

        # No 16
        little_max = Card(16, "Max", "None", "None", "deck", True)
        self.characters.append(little_max)

        # No 17
        kiba = Card(17, "Kiba", "None", "None", "deck", True)
        self.characters.append(kiba)

    def get_card_by_id(self, id):
        for card in self.characters:
            if card.id == id:
                return card

    def add_card_to_deck(self, card):
        """
        Add a card to the deck.

        Args:
            card (Card): The card to be added to the deck.
        """
        self.deck.append(card)

    def lvl1(self):
        playing_characters = [self.get_card_by_id(1),self.get_card_by_id(15), self.get_card_by_id(2), self.get_card_by_id(16)]
        for card in playing_characters:
            self.add_card_to_deck(card)

    def bubble_sort_cards_by_id(self, card_list):
        """
        Sort a list of cards by their id using the bubble sort algorithm.

        Args:
            card_list (list): The list of cards to be sorted.
        """
        n = len(card_list)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if card_list[j].id > card_list[j + 1].id:
                    # Swap the cards
                    card_list[j], card_list[j + 1] = card_list[j + 1], card_list[j]

    def move_card(self, source, destination, card):
        """
        Move a card from one array to another.

        Args:
            source (list): The source card array.
            destination (list): The destination card array.
            card (Card): The card to move.

        Raises:
            ValueError: If the card is not found in the source array.
        """
        if card in source:
            source.remove(card)
            destination.append(card)
        else:
            raise ValueError("Card not found in the source array.")

    def display_cards(self, location):
        """
        Display the cards in a specified location.

        Args:
            location (list): The card array to display.

        Returns:
            str: A formatted string listing the cards.
        """
        return "\n".join(card.display_card() for card in location)

    def shuffle_deck(self):
        """
        Shuffle the deck of cards.
        """
        import random
        random.shuffle(self.deck)

    def __repr__(self):
        """
        Return a string representation of the game state.
        """
        return (
            f"Game(deck={len(self.deck)} cards, "
            f"basement={len(self.basement)} cards, "
            f"red_room={len(self.red_room)} cards, "
            f"blue_room={len(self.blue_room)} cards)"
        )

    def draw_from_deck(self):
        """
        Draw the first card from the deck and print its details.
        The card is removed from the deck.
        Raises:
        ValueError: If the deck is empty.
        """
        if not self.deck:
            raise ValueError("The deck is empty! No cards to draw.")
        
        card = self.deck.pop(0)
        print("Drew card:")
        print(card.display_card())
        return card
    
    def back_to_deck(self, card, current_room):
        """
        Move a card from its current room back to the other room.

        Args:
            card (Card): The card to move.
            current_room (list): The current room of the card.

        Raises:
            ValueError: If the card is not found in the current room.
        """
        if current_room == self.red_room:
            self.red_room.remove(card)
            self.blue_room.append(card)
        elif current_room == self.blue_room:
            self.blue_room.remove(card)
            self.red_room.append(card)
        else:
            raise ValueError("Invalid current room specified or card not found.")

    def switch_room(self, card, current_room):
        if current_room == self.red_room:
            self.red_room.remove(card)
            self.blue_room.append(card)
        elif current_room == self.blue_room:
            self.blue_room.remove(card)
            self.red_room.append(card)
        else:
            raise ValueError(f"Card no {card.id} was not found in {card.place}.")

    def show_room(self, room):
        print(f"Inside {room} are the following cards:")
        for card in room:
            print(card.id)
        
