from typing import List
from Card import Card

class Game:
    def __init__(self, characters: List[Card]):
        self.deck: List[Card] = []
        self.basement: List[Card] = []
        self.red_room: List[Card] = []
        self.blue_room: List[Card] = []
        self.characters: List[Card] = characters

    def bubble_sort_cards_by_id(self, card_list: List[Card]):
        n = len(card_list)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if card_list[j].id > card_list[j + 1].id:
                    card_list[j], card_list[j + 1] = card_list[j + 1], card_list[j]

    def apply_skill(self, card: Card, room: List[Card]) -> bool:
        if not card.skill:
            return False

        condition_met = False
        value = card.skill.get("value")

        if card.condition == "min_cards" and len(room) <= value:
            condition_met = True
        elif card.condition == "max_cards" and len(room) >= value:
            condition_met = True
        elif card.condition == "min_green" and sum(1 for c in room if c.good) >= value:
            condition_met = True
        elif card.condition == "specific_card" and any(c.id == value for c in room):
            condition_met = True
        elif card.condition is None:
            condition_met = True

        if not condition_met:
            return False

        target = None
        target_type = card.skill["target"]

        if target_type == "highest_green":
            target = max((c for c in room if c.good), key=lambda c: c.id, default=None)
        elif target_type == "lowest_red":
            target = min((c for c in room if not c.good), key=lambda c: c.id, default=None)
        elif target_type == "specific_card":
            target = next((c for c in room if c.id == value), None)

        if not target:
            return False

        effect = card.skill["effect"]
        targets = [target] if not isinstance(target, list) else target

        if effect == "injure":
            for t in targets:
                if t in room:
                    room.remove(t)
                    self.basement.append(t)
            return True
        elif effect == "move_to_deck_bottom":
            for t in targets:
                if t in room:
                    room.remove(t)
                    self.deck.append(t)
        elif effect == "move_other_room":
            for t in targets:
                if t in self.red_room:
                    self.red_room.remove(t)
                    self.blue_room.append(t)
                elif t in self.blue_room:
                    self.blue_room.remove(t)
                    self.red_room.append(t)

        return False

    def resolve_room(self, room: List[Card]):
        self.bubble_sort_cards_by_id(room)
        for card in room[:]:
            self.apply_skill(card, room)

    def resolve_turn(self, room: List[Card]) -> str:
        before = set(card.id for card in self.basement)
        self.resolve_room(room)
        after = set(card.id for card in self.basement)
        new_injured_ids = after - before

        if not new_injured_ids:
            return "SILENCIO"
        elif 6 in new_injured_ids:
            return "FUGA"
        else:
            return "SANGRE"

    def move_card(self, source: List[Card], destination: List[Card], card: Card):
        if card in source:
            source.remove(card)
            destination.append(card)
        else:
            raise ValueError("Card not found in the source array.")

    def shuffle_deck(self):
        import random
        random.shuffle(self.deck)

    def draw_from_deck(self) -> Card:
        if not self.deck:
            raise ValueError("The deck is empty! No cards to draw.")
        return self.deck.pop(0)

    def add_card_to_deck(self, card: Card):
        self.deck.append(card)

    def show_room(self, room: List[Card]):
        print(f"Room has cards: {[card.id for card in room]}")
