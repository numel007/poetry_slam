from random import choice
infile = open("poem.txt", "r")
lines_list = []

def get_file_lines(filename):
    line_count = 0
    for line in filename:
        line = line.rstrip("\n").split(":")
        lines_list.append(line)
        line_count += 1

    print("\n")

    return lines_list


def lines_printed_backwards(lines_list):
    for line_num, text in reversed(lines_list):
        print(line_num, text)
    print("\n")

def lines_printed_random(lines_list):
    randPoem = []
    poem_length = len(lines_list)
    for i in range(poem_length):
        randPoem.append(choice(lines_list))
        i += 1
    
    for line_num, text in randPoem:
        print(line_num, text)
    print("\n")


get_file_lines(infile)
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)