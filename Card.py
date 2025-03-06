class Card:
    """
    A class to represent a card with unique attributes.
    """

    def __init__(self, card_id, name, skill, condition, place, good):
        """
        Initialize a new Card instance.

        Args:
            card_id (int): Unique identifier for the card.
            name (str): Name of the card.
            skill (str): Skill associated with the card.
            condition (str): Condition or status of the card.
        """
        self.id = card_id
        self.name = name
        self.skill = skill
        self.condition = condition
        self.place = place
        self.good = good

    def __repr__(self):
        """
        Return a string representation of the Card instance.
        """
        return f"Card(id={self.id}, name='{self.name}', skill='{self.skill}', condition='{self.condition}', place='{self.place}')"

    def display_card(self):
        """
        Display the card's attributes in a formatted string.
        """
        return (
            f"Card ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Skill: {self.skill}\n"
            f"Condition: {self.condition}\n"
            f"Place: {self.place}\n"
        )

