"""
CHALLENGE: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
IMPLEMENTATION: Ignore Brute force algo and implement binary search
"""
from gettext import find


def find_card(deck, card):
    """
    find_card: function returns the position of a card in the deck
    @deck: the stack of cards
    @card: specific card
    """
    start_point = 0
    end_point = len(deck) - 1
    while start_point <= end_point:
        middle = (start_point + end_point) // 2
        middle_card = deck[middle]
        print(f"middle card: {middle_card}")
        if middle_card == card:
            return middle
        elif card < middle_card:
            end_point = middle - 1
        elif card > middle_card:
            start_point = middle + 1
    return -1

print(find_card([1,3,7,11,13,15,17,19], 191))