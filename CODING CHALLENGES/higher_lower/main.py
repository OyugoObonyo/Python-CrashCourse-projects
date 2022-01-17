"""
A console version of the famous higher_lower game
"""
import random
from data import data
from art import logo, vs

# Ensure question not repeating itself
# Generate random quesses
# Get user inputs
# Ensure random positions aren't similar
def get_index(list):
    index = random.randint(0, (len(data)-1))
    return index

def user_input():
    print("Who has more followers, A or B ? ")
    


def highest_followers(item1, item2):
    if item1['follower_count'] > item2 ['follower_count']:
        return item1
    else:
        return item2

if __name__ == '__main__':
    proceed = True
    points = 0
    while proceed:
        item_a = data[get_index(data)]
        item_b = data[get_index(data)]
        correct = highest_followers(item_a, item_b)
        
        print(logo)
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
        print(vs)
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
        count_guess = input("Who has more followers, A or B ? ")
        if count_guess == 'A':
            if item_a['follower_count'] > item_b['follower_count']:
                points += 1 
                print(f'You got that right! Current score: {points}\n')
            else:
                print(f'Sorry, that is wrong. Final score: {points}\n')
        elif count_guess == 'B':
            if item_b['follower_count'] > item_a['follower_count']:
                points += 1 
                print(f'You got that right! Current score: {points}\n')
            else:
                print(f'Sorry, Your answer is not correct. Final score: {points}\n')
                proceed = False
