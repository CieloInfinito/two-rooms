from dataclasses import dataclass
from typing import Optional, Dict, Union

@dataclass(frozen=True)
class Card:
    id: int
    name: str
    skill: Optional[Dict[str, Union[str, int]]] = None
    condition: Optional[str] = None
    good: bool = False

    def display_card(self) -> str:
        return (
            f"Card ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Skill: {self.skill}\n"
            f"Condition: {self.condition}\n"
        )