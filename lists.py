"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return list((number, number + 1, number + 2))


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    average = sum(hand) / len(hand)
    
    average_first_last = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]
    
    return average in {average_first_last, median}


def average_even_is_average_odd(hand):
    even_index_card = []
    odd_index_card = []
    
    for idx, value in enumerate(hand):
        if idx % 2 == 0:
            even_index_card.append(value)
        else:
            odd_index_card.append(value)
    
    if len(even_index_card) > 0:
        mean_even_index = sum(even_index_card) / len(even_index_card)
    else:
        mean_even_index = 0
    
    if len(odd_index_card) > 0:
        mean_odd_index = sum(odd_index_card) / len(odd_index_card)
    else:
        mean_odd_index = 0
    
    return mean_even_index == mean_odd_index
        


def maybe_double_last(hand):
    
    if hand[-1] == 11:
        hand[-1] = 22
    return hand

