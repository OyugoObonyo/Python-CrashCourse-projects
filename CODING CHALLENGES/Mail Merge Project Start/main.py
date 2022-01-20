# Create a letter using starting_letter.txt 
with open('./Input/Letters/starting_letter.txt') as file:
    contents = file.read()

#for each name in invited_names.txt
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

#Replace the [name] placeholder with the actual name.
for name in names:
    name = name.strip('\n')
    new_letter = contents.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
        file.write(new_letter)
