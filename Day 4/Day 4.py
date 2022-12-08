def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(data):
    my_file = readfile(data)
    array = my_file.split("\n")

    # split array at every ,
    array = [x.split(",") for x in array]

    # split every array at the -
    array = [[x[0].split("-"), x[1].split("-")] for x in array]

    # turn the strings into ints
    array = [[[int(x[0]), int(x[1])] for x in y] for y in array]

    # turn the array into a range of numbers from the first to the second number
    array = [[range(x[0][0], x[0][1] + 1), range(x[1][0], x[1][1] + 1)] for x in array]

    return array


def calculate_overlaps(array):
    # find the overlap between the two ranges
    overlap = [set(x[0]).intersection(set(x[1])) for x in array]

    # find the length of the overlap
    overlap = [len(x) for x in overlap]

    # find the overlaps where the overlap is greater or equal to the length of the first or second range
    amount_full = [x >= len(array[i][0]) or x >= len(array[i][1]) for i, x in enumerate(overlap)]

    # find all overlaps
    amount_partial = [x > 0 for x in overlap]

    # return the number of overlaps
    return sum(amount_full), sum(amount_partial)


print(calculate_overlaps(dataprep("Test.txt")))
print(calculate_overlaps(dataprep("Puzzle.txt")))

