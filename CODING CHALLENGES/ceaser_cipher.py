"""
Encodes and decodes texts based on ceaser's cipher
"""
from hangman import convert_to_list

def encode(text, shift):
    text = convert_to_list(text)
    word_l = []
    for i in range(len(text)):
        if text[i] == " ":
            word_l.append(text[i])
        else:
            ord_val = ord(text[i]) + shift
            if ord_val > 122:
                ord_val = (ord(text[i]) - 26) + shift
            text[i] = chr(ord_val)
            word_l.append(text[i])
    word_l = "".join(map(str, word_l))
    return word_l

def decode(text, shift):
    text = convert_to_list(text)
    word_l = []
    for i in range(len(text)):
        if text[i] == " ":
            word_l.append(text[i])
        else:
            ord_val = ord(text[i]) - shift
            text[i] = chr(ord_val)
            word_l.append(text[i])
    word_l = "".join(map(str, word_l))
    return word_l

if __name__ == "__main__":
    repl = True

    while repl:
        control = input("Do you want to encode or decode\n").lower()
        if control == "decode":
            text = input("Enter text you want to decode\n")
            shift = int(input("Enter the shift number\n"))
            print(f"Here is the decode text: {decode(text, shift)}")
        elif control == "encode":
            text = input("Enter text you want to encode\n")
            shift = int(input("Enter the shift number\n"))
            print(f"Here is the encoded text: {encode(text, shift)}")
        proceed = input(" Would you like to proceed? 'yes' or 'no'\n")
        if proceed == "yes" :
            continue
        else:
            repl = False
