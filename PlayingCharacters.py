from dataclasses import dataclass, field
from typing import List
from Card import Card

@dataclass
class PlayingCharacters:
    no_1: Card = field(default_factory=lambda: Card(1, "Mouse"))
    no_2: Card = field(default_factory=lambda: Card(2, "Frog"))

    # no 3

    no_4: Card = field(default_factory=lambda: Card(
        4, "N4", {"target": "highest_green", "effect": "move_to_deck_bottom", "value": 2},
        "min_green", False))
    no_5: Card = field(default_factory=lambda: Card(
        5, "Cindirella", {"target": "specific_card", "effect": "injure", "value": 14},
        "specific_card", False))
    no_6: Card = field(default_factory=lambda: Card(
        6, "Harman", {"target": "highest_green", "effect": "injure", "value": 3},
        "max_cards", False))
    
    # no 7

    no_8: Card = field(default_factory=lambda: Card(
        8, "Lance", {"target": "lowest_red", "effect": "move_other_room", "value": 3},
        None, False))
    
    # no 11

    # no 12


    no_13: Card = field(default_factory=lambda: Card(
        13, "girlfriend", {"target": "lowest_red", "effect": "injure", "value": 11},
        "specific_card", True))
    no_14: Card = field(default_factory=lambda: Card(
        14, "Nathan", {"target": "lowest_red", "effect": "injure", "value": 3},
        "max_cards", True))
    no_15: Card = field(default_factory=lambda: Card(15, "Nina", None, None, True))
    no_16: Card = field(default_factory=lambda: Card(16, "Max", None, None, True))
    no_17: Card = field(default_factory=lambda: Card(17, "Kiba", None, None, True))
    
    @property
    def characters(self) -> List[Card]:
        return [
            self.no_1, self.no_2, self.no_4, self.no_5, self.no_6, self.no_8,
            self.no_13, self.no_14, self.no_15, self.no_16, self.no_17
        ]