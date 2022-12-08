import numpy as np

def read_input(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep_general(data):
    my_file = read_input(data)
    array = my_file.split("\n")
    array = np.array(array)

    return array


def dataprep_compartments(data):
    array = dataprep_general(data)
    # divide each string into a list of chars
    array = [list(x) for x in array]
    # divide each list of chars into 2 lists of chars
    array = [np.array_split(x, 2) for x in array]
    first_compartments = [x[0] for x in array]
    second_compartments = [x[1] for x in array]

    # return the chars that are the same in both compartments for every array in the compartments
    array = [np.intersect1d(first_compartments[i], second_compartments[i]) for i in range(len(first_compartments))]

    # change the array of arrays into a single array
    array = np.concatenate(array)

    return array


def dataprep_groups(data):
    array = dataprep_general(data)

    # split the array after every third element
    array = np.split(array, np.arange(3, len(array), 3))

    # divide each string into a list of chars
    for i in range(len(array)):
        array[i] = [list(x) for x in array[i]]

    # find the 1 char that is the same in every string
    for i in range(len(array)):
        chars = np.intersect1d(array[i][0], array[i][1])
        array[i] = np.intersect1d(chars, array[i][2])

    # change the array of arrays into a single array
    array = np.concatenate(array)

    return array


def calculate_priority(array):
    # the priority is the index of the char in the alphabet
    # capital letters start at 27, lowercase letters start at 1

    priority = 0

    for i in range(len(array)):
        if "A" <= array[i] <= "Z":
            priority += ord(array[i]) - 38
        elif "a" <= array[i] <= "z":
            priority += ord(array[i]) - 96
    return priority


print(calculate_priority(dataprep_compartments("Test Input.txt")))
print(calculate_priority(dataprep_compartments("Puzzle Input.txt")))


print(calculate_priority(dataprep_groups("Test Input.txt")))
print(calculate_priority(dataprep_groups("Puzzle Input.txt")))
