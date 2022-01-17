"""
A console version of the famous higher_lower game
"""
import random
from data import data
from art import logo, vs


def compare_dicts(data, dict_1, dict_2):
    """
    Function compares two dicts to ensure the randomly selected
    dicts are not similar
    """
    while dict_2 == dict_1:
        dict_2 == random.choice(data)


def check_guess(guess, followers_a, followers_b):
    """
    Function that evaluates a user's guess
    """
    if guess == 'A' and followers_a > followers_b:
        return True
    elif guess == 'B' and followers_a < followers_b:
        return True
    else:
        return False


proceed = True
points = 0
while proceed:
    if points == 0:
        item_a = random.choice(data)
    else:
        item_a = item_b
    item_b = random.choice(data)
    compare_dicts(data, item_a, item_b)

    print(logo)
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(vs)
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
    count_guess = input("Who has more followers, A or B ? ")
    is_correct = check_guess(count_guess, item_a['follower_count'], item_b['follower_count'] )
    if is_correct:
        points += 1
        print(f'You got that right! Current score: {points}\n')
    else:
        print(f'Sorry, your answer is not correct. Final score: {points}\n')
        proceed = False