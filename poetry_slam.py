# Import random module and choice method from random module
from random import choice
import random

# Initialize an empty dictionary
lines_list = {}

def get_file_lines(filename):
    # Open input file and store contents in variable lines
    with open(filename, "r") as openfile:
        lines = openfile.readlines()
    # Iterate through lines
    for line in lines:
        # Split each line at ":" and remove line breaks. Store in a list called split_poem
        split_poem = line.rstrip().rsplit(":")
        # Store index 0 of split_poem in line_num for future reference
        line_num = split_poem[0]
        # Store index 1 of split_poem in poem_text for future reference
        poem_text = split_poem[1]
        # Add keys and values of line_num and poem_text into dictionary, respectively 
        lines_list[line_num] = poem_text
    
    return lines_list


def lines_printed_backwards(lines_list):
    # Iterate through lines_list and print each line backwards, using the reversed method
    for line_num, text in reversed(lines_list.items()):
        print(line_num, text)

    print("\n")

def lines_printed_random(lines_list):
    # Initialize new dictionary
    randPoem = {}
    # Get number of lines in poem
    poem_length = len(lines_list)

    for i in range(poem_length):
        # Convert lines_list into a list and scramble with choice. Store in randPoem dictionary.
        randPoem[i] = choice(list(lines_list.items()))
        i += 1

    # Print just the values stored in randPoem, which include the original keys from lines_list for reference.
    for line_num, text in randPoem.items():
        print(text)
    print('\n')

# The custom function scrambles all the words in each line of the poem.
def lines_printed_custom(lines_list):
    # Convert lines_list into list and store in lines_list_custom
    lines_list_custom = list(lines_list.items())
    # Scramble lines_list_custom using shuffle method
    random.shuffle(lines_list_custom)
    # Convert lines_list_custom into dictionary and store in lines_list
    lines_list = dict(lines_list_custom)

    # Print values of lines_list dictionary
    for i in lines_list:
        print(lines_list[i])

# Call functions
get_file_lines('poem.txt')
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)
lines_printed_custom(lines_list)