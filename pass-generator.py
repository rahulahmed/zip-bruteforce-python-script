#use this file to generate custome password list. Password list will require for bruteforce password.
import itertools

# Define the characters to use: 0-9, A-Z, and a-z
characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Create all possible 6-character combinations
combinations = itertools.product(characters, repeat=4)

# Write to file (optional: to avoid generating an enormous file)
with open('rahul.txt', 'w') as file:
    for combination in combinations:
        file.write(''.join(combination) + '\n')
