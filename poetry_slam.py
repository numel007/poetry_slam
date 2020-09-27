infile = open("poem.txt", "r")
poem_lines = []

def get_file_lines(filename):
    line_count = 0
    for line in filename:
        line = line.split(":")
        print(line)
        poem_lines.append(line)
        line_count += 1
    print(f"{line_count} lines")

    return poem_lines

get_file_lines(infile)

# def lines_printed_backwards(filename):
    


# lines_printed_backwards(infile)