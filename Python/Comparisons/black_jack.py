"""Functions to help play and score a game of blackjack.
How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


values = {'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9, '8': 8, '7': 7,
          '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}


def value_of_card(card):
    """Determine the scoring value of a card.
    :param card: str - given card.
    :return: int - value of a given card.  See below for values.
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    return values[card]


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if values[card_one] == values[card_two]:
        return card_one, card_two
    return max(vars().values(), key=lambda x: values[x])


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    vals = values.copy()
    vals['A'] = 11 if 'A' in vars().values() else 1
    return 1 if vals[card_one] + vals[card_two] > 10 else 11


def is_blackjack(*args):
    """Determine if the hand is a 'natural' or 'blackjack'.
    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    return ''.join(args) in 'AKAQAJA10A'


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are
    of the same value).
    """
    return values[card_one] == values[card_two]


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or
    11 points).
    """
    return 8 < values[card_one] + values[card_two] < 12
