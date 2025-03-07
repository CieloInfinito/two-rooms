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
        mouse = Card(21, "Mouse", None, None, "deck", False)
        self.characters.append(mouse)
        
        # No 2
        frog = Card(2, "Frog", None, None, "deck", False)
        self.characters.append(frog)
        
        # No 3
        # josh = Card(3, "Joshua", skill, "max_cards", "deck", False)
        # self.characters.append(josh)

        skill_4={"target": "highest_green", "effect": "move_to_deck_bottom", "value": 2}

        # No 4
        travis = Card(4, "N4", skill_4, "min_green", "deck", False)
        self.characters.append(travis)

        skill_5={"target": "specific_card", "effect": "injure", "value": 14}

        # No 5
        cindi = Card(5, "Cindirella", skill_5, "specific_card", "deck", False)
        self.characters.append(cindi)

        skill_6={"target": "highest_green", "effect": "injure", "value": 3}

        # No 6
        harman = Card(6, "Harman", skill_6, "min_cards", "deck", False)
        self.characters.append(harman)

        # skill_7={"target": "specific_pair", "effect": "injure", "value": 15}

        # # No 7
        # chick = Card(7, "Some_chick", skill_7, "specific_card", "deck", False)
        # self.characters.append(chick)
        
        skill_8={"target": "lowest_red", "effect": "move_other_room", "value": 3}

        # No 8
        bad_boy = Card(8, "Lance", skill_8, None, "deck", False)
        self.characters.append(bad_boy)
        
        # Good guys
        # No 11
        # boyfriend = Card(11, "boyfriend", skill, "None", "deck", True)
        # self.characters.append(boyfriend)

        # No 12
        # bond = Card(12, "bond", skill, "None", "deck", True)
        # self.characters.append(bond)

        skill_13={"target": "lowest_red", "effect": "injure", "value": 11}

        # No 13
        girlfriend = Card(13, "girlfriend", skill_13, "specific_card", "deck", True)
        self.characters.append(girlfriend)

        skill_14={"target": "lowest_red", "effect": "injure", "value": 3}

        # No 14
        nathan = Card(14, "Nathan", skill_14, "max_cards", "deck", True)
        self.characters.append(nathan)

        # No 15
        nina = Card(15, "Nina", None, None, "deck", True)
        self.characters.append(nina)

        # No 16
        little_max = Card(16, "Max", None, None, "deck", True)
        self.characters.append(little_max)

        # No 17
        kiba = Card(17, "Kiba", None, None, "deck", True)
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
        print("Card added to deck:")
        print(card)
        self.deck.append(card)
    
    def add_card_to_room(self, card, room):
        """Adds a card to the specified room."""
        if room not in [self.red_room, self.blue_room]:
            raise ValueError("Invalid room specified")
        
        if room is self.red_room:
            card.place = "red_room"
        if room is self.blue_room:
            card.place = "blue_room"
        print(f"Card added to {card.place}:")
        print(card)
        room.append(card)

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
        
    def apply_skill(self, card, room):
        """Applies a card's skill based on its condition and target."""
        if not card.skill:
            return

        # Determine if condition is met
        condition_met = False
        if card.condition == "min_cards" and len(room) <= card.skill["value"]:
            condition_met = True
        elif card.condition == "max_cards" and len(room) >= card.skill["value"]:
            condition_met = True
        elif card.condition == "min_green" and sum(1 for c in room if c.good) >= card.skill["value"]:
            condition_met = True
        elif card.condition == "specific_card" and any(c.id == card.skill["value"] for c in room):
            condition_met = True
        elif card.condition is None:
            condition_met = True  # No condition required

        if not condition_met:
            return

        # Determine target based on skill
        target = None
        if card.skill["target"] == "next_deck":
            if self.deck:
                target = self.deck[0]
        elif card.skill["target"] == "highest_green":
            target = max((c for c in room if c.good), key=lambda c: c.id, default=None)
        elif card.skill["target"] == "lowest_red":
            target = min((c for c in room if not c.good), key=lambda c: c.id, default=None)
        # elif card.skill["target"] == "specific_pair":
        #     if all(self.get_card_by_id(cid) in room for cid in card.skill["value"]):
        #         target = [self.get_card_by_id(cid) for cid in card.skill["value"]]
        elif card.skill["target"] == "any":
            target = room  # Affect all cards in the room
        elif card.skill["target"] == "specific_card":
            target = card.skill["value"]

        if not target:
            return

        # Apply skill effect
        if card.skill["effect"] == "move_other_room":
            for t in (target if isinstance(target, list) else [target]):
                self.switch_room(t, room)
        elif card.skill["effect"] == "move_to_deck_bottom":
            for t in (target if isinstance(target, list) else [target]):
                self.deck.append(t)
                room.remove(t)
        elif card.skill["effect"] == "injure":
            for t in (target if isinstance(target, list) else [target]):
                t.place = "basement"
                self.basement.append(t)
                room.remove(t)
                return True
        elif card.skill["effect"] == "move_to_room":
            for t in (target if isinstance(target, list) else [target]):
                room.append(t)

        return False

    def resolve_room(self, room):
        self.bubble_sort_cards_by_id(room)
        injured = []
        
        for card in room[:]:
            if self.apply_skill(card, room): injured.append(card)
        
        if injured:
            if any(card.id == 6 for card in injured):
                return "FUGA"
            return "SANGRE"
        return "SILENCIO"