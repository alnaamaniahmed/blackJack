from Constants import values


class Hand:
    """
    A class representing a hand of playing cards in a card game.

    Attributes:
        cards (list): A list of Card objects in the hand.
        value (int): The total value of the hand based on the ranks of the cards.
        aces (int): The count of Ace cards in the hand.

    Methods:
        add_card(self, card):
            Adds a card to the hand and updates the hand's value accordingly.

        adjust_for_ace(self):
            Adjusts the hand's value to account for the value of Ace cards when necessary.
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)  # Add a card to the hand
        # Update the hand's value based on the added card's rank
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        if self.value > 21 and self.aces:
            self.value -= 10  # Adjust the value by subtracting 10 to account for the Ace being 1
            self.aces -= 1
