"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

TEN_CARD=['Q','J','K','L','10']

def value_of_card(card):
    """Determine the scoring value of a card.
    """
    
    if card in TEN_CARD :
        return 10
    if card == 'A' :
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.
    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    if card_one == 'A' or card_two == 'A':
        return 1
    if (value_of_card(card_one) + value_of_card(card_two) + 11) > 21 :
        return 1
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """ 
    if card_one == 'A' and card_two in TEN_CARD :
        return True
    if card_two == 'A' and card_one in TEN_CARD :
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
    Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if 11 >= (value_of_card(card_one) + value_of_card (card_two)) >= 9:
        return True
    return False