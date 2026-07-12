#assignment 1

# Create an output dictionary containing only
# the odd numbers as keys and their cubes as values.

list_1 = [1, 2, 3, 4, 5, 6, 7]

result = {x: x**3 for x in list_1 if x % 2 != 0}

print(result)

#assignment 2

# Make a dictionary of the 26 English alphabets
# mapping each with the corresponding integer.

import string

alphabet_dict = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}

print(alphabet_dict)
