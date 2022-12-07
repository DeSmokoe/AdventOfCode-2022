import numpy as np

def readfile(filename):
    input_file = open(filename, "r")
    return input_file.read()


def dataprep(data):
    my_file = readfile(data)
    array = my_file.split("\n")

    for i in range(len(array)):
        if array[i] == "":
            array[i] = 0
        else:

            array[i] = int(array[i])

    array = np.array(array)
    return array


def find_maximum(array):

    # split the array at every 0
    array = np.split(array, np.where(array == 0)[0])

    # remove all the 0s in the arrays
    array = [x[x != 0] for x in array]

    # take the sum of each array
    array = [np.sum(x) for x in array]

    return max(array)


def find_top_3(array):
    # split the array at every 0
    array = np.split(array, np.where(array == 0)[0])

    # remove all the 0s in the arrays
    array = [x[x != 0] for x in array]

    # take the sum of each array
    array = [np.sum(x) for x in array]

    return sum(sorted(array, reverse=True)[:3])


print(find_maximum(dataprep("Puzzle Input.txt")))
print(find_top_3(dataprep("Puzzle Input.txt")))
