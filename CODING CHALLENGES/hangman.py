"""
A console version of the popular game, hangman
"""
import random


# Generate random word
WORDS = [
    'camel', 'buffalo', 'schadenfreude', 'premier', 'gallop', 'hubris',
    'enamel', 'pretzel', 'temerity']


def convert_to_list(string):
    """
    Converts a string to a list
    """
    list = []
    list[:0] = string
    return list


if __name__ == '__main__':
    word = random.choice(WORDS)
    word_l = convert_to_list(word)
    lives = len(word)
    points = 0
    display = []
    for ch in word:
        display.append('_')
    while lives:
        guess = input('What letter could be in our word? ').lower()
        for i in range(len(word)):
            if word[i] == guess:
                points += 1
                display[i] = guess
        print(display)
        lives -= 1
        if word_l == display:
            break
        print(f'Points: {points}')
        print(f'Lives: {lives}')
    print(f"Congratulations! You got the word right!")
