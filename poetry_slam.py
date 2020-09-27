infile = open("poem.txt", "r")
lines_list = []

def get_file_lines(filename):
    line_count = 0
    for line in filename:
        line = line.rstrip("\n").split(":")
        lines_list.append(line)
        line_count += 1

    return lines_list


def lines_printed_backwards(lines_list):
    for line_num, text in reversed(lines_list):
        print(line_num, text)


get_file_lines(infile)
lines_printed_backwards(lines_list)