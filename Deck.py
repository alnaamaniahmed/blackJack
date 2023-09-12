import random
from Constants import suits, ranks
from Card import Card


class Deck:
    """
    A class representing a deck of playing cards.

    Attributes:
        deck (list): A list of Card objects representing the deck.

    Methods:
        shuffle(self):
            Shuffles the deck randomly.

        deal(self):
            Removes and returns the last card in the deck.

        __str__(self):
            Returns a string representation of the deck.
    """

    def __init__(self):
        self.deck = []  # Initialize an empty list to hold cards
        for suit in suits:
            for rank in ranks:
                # Create and add Card objects to the deck
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_card = self.deck.pop()
        return deal_card

    def __str__(self):

        cards_in_deck = ''
        for card in self.deck:
            cards_in_deck += '\n ' + card.__str__()
        return f'The deck has {len(self.deck)} cards which are: {cards_in_deck}'
