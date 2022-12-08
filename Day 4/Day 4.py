import pandas as pd


def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(data):
    my_file = readfile(data)
    array = my_file.split("\n")
    array = pd.Series(array)

    # split the array in 2 at every comma and "-"
    array = array.str.split(",", expand=True)

    # split the array in 2 at every "-"
    array = array.stack().str.split("-", expand=True).unstack()


    # expand the array to a list starting from the first int to the last
    #array = array.apply(lambda x: list(range(int(x[0]), int(x[1]) + 1)), axis=1)

    print(array)


dataprep("Test.txt")