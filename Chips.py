class Chips:
    """
    A class representing a player's chips for betting in a card game.

    Attributes:
        total (int): The total number of chips the player has.
        bet (int): The current bet amount.

    Methods:
        win_bet(self):
            Increases the total chips when the player wins the bet.

        lose_bet(self):
            Decreases the total chips when the player loses the bet.
    """

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
