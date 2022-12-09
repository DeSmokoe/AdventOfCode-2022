import pandas as pd

def readfile(puzzle=False):
    if puzzle:
        filename = "Puzzle.txt"
    else:
        filename = "Test.txt"
    with open(filename, "r") as f:
        return f.read()

def data_prep(puzzle=False):

    # create a dataframe from readfile
    data = pd.DataFrame(readfile(puzzle).splitlines())
    # split each character in the dataframe into a new column
    data = data[0].str.split("", expand=True)
    # remove the first column
    data = data.iloc[:, 1:]
    # remove the last column
    data = data.iloc[:, :-1]
    # rename the columns
    data.columns = range(data.shape[1])
    # change all the values to integers
    data = data.astype(int)

    return data

def locate_highest_trees(puzzle=False):
    data = data_prep(puzzle)

    # create a copy of the dataframe filled with 0
    trees = pd.DataFrame(0, index=data.index, columns=data.columns)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data.iloc[i, j] > data.iloc[:i, j].max() or data.iloc[i, j] > data.iloc[i+1:, j].max() or data.iloc[i, j] > data.iloc[i, :j].max() or data.iloc[i, j] > data.iloc[i, j+1:].max():
                trees.iloc[i, j] = 1
            if i == 0 or i == data.shape[0]-1 or j == 0 or j == data.shape[1]-1:
                trees.iloc[i, j] = 1

    amount = trees.sum().sum()
    print(amount)

def calculate_scenic_score(puzzle=False):

    data = data_prep(puzzle)

    scenic_scores = pd.DataFrame(1, index=data.index, columns=data.columns)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            trees = pd.DataFrame(0, index=data.index, columns=data.columns)

            # blocked from below
            for k in range(i + 1, data.shape[0]):
                if data.iloc[k, j] >= data.iloc[i, j]:
                    trees.iloc[k, j] = 1
                    scenic_scores.iloc[i, j] *= k - i
                    break
                elif k == data.shape[0] - 1:
                    scenic_scores.iloc[i, j] *= k - i

            # blocked from above
            for k in range(i-1, -1, -1):
                if data.iloc[k, j] >= data.iloc[i, j]:
                    trees.iloc[k, j] = 1
                    scenic_scores.iloc[i, j] *= i - k
                    break
                elif k == 0:
                    scenic_scores.iloc[i, j] *= k + 1

            # blocked from right
            for k in range(j + 1, data.shape[1]):
                if data.iloc[i, k] >= data.iloc[i, j]:
                    trees.iloc[i, k] = 1
                    scenic_scores.iloc[i, j] *= k - j
                    break
                elif k == data.shape[1] - 1:
                    scenic_scores.iloc[i, j] *= k - j

            # blocked from left
            for k in range(j-1, -1, -1):
                if data.iloc[i, k] >= data.iloc[i, j]:
                    trees.iloc[i, k] = 1
                    scenic_scores.iloc[i, j] *= j - k
                    break
                elif k == 0:
                    scenic_scores.iloc[i, j] *= j

            # Make all scenic scores 0 on the edges
            if i == 0 or i == data.shape[0]-1 or j == 0 or j == data.shape[1]-1:
                scenic_scores.iloc[i, j] = 0

    print(scenic_scores.max().max())


locate_highest_trees()
locate_highest_trees(True)

calculate_scenic_score()
calculate_scenic_score(True)



