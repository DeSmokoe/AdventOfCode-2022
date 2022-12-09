def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def find_markers(data):
    my_file = readfile(data)

    # find the first combination of four subsequent different letters with no duplicates
    for i in range(len(my_file)):
        if len(set(my_file[i:i + 4])) == 4:
            print(my_file[i:i + 4], i+4)
            break

    for j in range(len(my_file)):
        if len(set(my_file[j:j + 14])) == 14:
            print(my_file[j:j + 14], j+14)
            break


find_markers("Test.txt")
find_markers("Puzzle.txt")