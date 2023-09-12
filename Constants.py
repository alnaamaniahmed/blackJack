"""
A module defining constants and values for a Blackjack game.

Attributes:
    suits (tuple): A tuple containing the possible suits of playing cards.
    ranks (tuple): A tuple containing the ranks of playing cards.
    values (dict): A dictionary mapping card ranks to their corresponding values.
"""

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')


ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}
