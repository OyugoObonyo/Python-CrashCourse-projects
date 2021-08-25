"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.
"""


def alphabet_position(text):
    pos = []
    if not isinstance(text, str):
        return "FUNCTION ONLY ACCEPTS STRINGS AS ARGUEMENTS"
    for alph in text:
        if alph.isalpha():
            alph = ord(alph.lower())-96
            pos.append(alph)
        else:
            continue
    # Use map to convert list to string
    to_string = ' '.join(map(str, pos))
    return to_string