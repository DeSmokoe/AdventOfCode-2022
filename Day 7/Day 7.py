def readfile(puzzle=False):
    if puzzle:
        filename = "Puzzle.txt"
    else:
        filename = "Test.txt"
    with open(filename, "r") as f:
        return f.read()


def data_prep():
    array = readfile().splitlines()

    for i in range(len(array)):
        # Check if the line start with $
        if array[i][0] == "$":
            command(array[i][2:])
        elif array[i][:3] == "dir":
            save_directory(array[i][4:])
        else:
            save_file(array[i])

def command(line):
    pass

def save_file(line):
    pass

def save_directory(line):
    pass








data_prep()