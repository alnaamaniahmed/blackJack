from Deck import Deck
from Hand import Hand
from Chips import Chips

# Initialize the playing state
playing = True

# Function to take a bet from the player


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, this is not an integer!')
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed ', chips.total)
            else:
                break

# Function to add a card to the player's hand


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()

# Function for the player to choose to hit or stand


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        choice = input('Would you like to hit or stand? Enter h or s: ')
        if choice[0].lower() == 'h':
            hit(deck, hand)
        elif choice[0].lower() == 's':
            print('Player stands, Dealer is playing!')
            playing = False
        else:
            print('Sorry, Please try again.')
            continue
        break

# Function to show some of the cards


def show_some(player, dealer):
    # Dealer cards
    print("\n Dealer's hand: ")
    print("First card is hidden!")
    print(dealer.cards[1])

    # Player cards
    print("\n Player's hand: ", *player.cards, sep="\n")

# Function to show all cards


def show_all(player, dealer):
    print("\n Dealer's hand: ", *dealer.cards, sep="\n")
    print("Total value of the dealer's deck is ", dealer.value)
    print("\n Player's hand: ", *player.cards, sep="\n")
    print("Total value of the player's deck is ", player.value)

# Function for when the player busts


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

# Function for when the player wins


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

# Function for when the dealer busts


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.lose_bet()

# Function for when the dealer wins


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.win_bet()

# Function for a tie (push)


def push(player, dealer, chips):
    print('Player and Dealer tie! It is a push.')


# Main game loop
while True:
    print("Welcome to BlackJack Game ♥♦♣♠! Do not go over 21. \n\
          Dealer hits until they reach 17. Ace count as 1 or 11")

    # Create & shuffle the deck, deal two cards to each player
    deck_created = Deck()
    deck_created.shuffle()
    # Create player hand and deal two cards
    player_hand = Hand()
    player_hand.add_card(deck_created.deal())
    player_hand.add_card(deck_created.deal())
    # Create dealer hand and deal two cards
    dealer_hand = Hand()
    dealer_hand.add_card(deck_created.deal())
    dealer_hand.add_card(deck_created.deal())
    # Set up the Player's chips
    player_chips = Chips()
    # Prompt the Player for their bet
    take_bet(player_chips)
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck_created, player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck_created, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand, player_chips)

    # Inform Player of their chips total
    print("Player's winning standing:  ", player_chips.total)

    # Ask to play another hand
    game_off_on = input('Would you like to play another hand? Yes/No ')
    if game_off_on[0].upper() == 'Y':
        playing = True
        continue
    print('Thank you for playing!')
    break
