def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def find_marker(data, chars):
    my_file = readfile(data)

    # Find the first combination of x subsequent different letters
    for i in range(len(my_file)):
        if len(set(my_file[i:i + chars])) == chars:
            print(my_file[i:i + chars], i + chars)
            break


find_marker("Test.txt", 4)
find_marker("Test.txt", 14)
find_marker("Puzzle.txt", 4)
find_marker("Puzzle.txt", 14)