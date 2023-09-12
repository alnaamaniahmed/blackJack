class Card:
    """
    A class representing a playing card.

    Attributes:
        suit (str): The suit of the card.
        rank (str): The rank of the card.

    Methods:
        __init__(self, suit, rank):
            Initializes a Card with a given suit and rank.

        __str__(self):
            Returns a string representation of the Card.
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
