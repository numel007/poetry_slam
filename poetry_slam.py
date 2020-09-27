infile = open("poem.txt", "r")
poem_lines = []

def get_file_lines(filename):
    line_count = 0
    for line in filename:
        line = line.rstrip("\n").split(":")
        poem_lines.append(line)
        line_count += 1

    return poem_lines


def lines_printed_backwards(filename):
    for line_num, text in reversed(poem_lines):
        print(line_num, text)

get_file_lines(infile)
lines_printed_backwards(infile)