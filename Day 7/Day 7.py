import pandas as pd
import numpy as np


def readfile(puzzle=False):
    if puzzle:
        filename = "Puzzle.txt"
    else:
        filename = "Test.txt"
    with open(filename, "r") as f:
        return f.read()


def data_prep():
    terminal_output = readfile().splitlines()
    fs = pd.DataFrame({"Remove": [1]})  # File Structure
    cd = ""  # Current Directory

    for i in range(len(terminal_output)):
        # Check if the line start with $
        if terminal_output[i][0] == "$":
            fs, cd = command(terminal_output[i][2:], fs, cd)
        elif terminal_output[i][:3] == "dir":
            fs = save_directory(terminal_output[i][4:], fs, cd)
        else:
            save_file(terminal_output[i], fs, cd)

    # remove the first column of fs
    fs = fs.iloc[:, 1:]

    return fs


def command(output_line, fs, cd):
    if output_line[:2] == "cd":
        fs, cd = change_directory(output_line[3:], fs, cd)
    elif output_line[:2] == "ls":
        list_content()
    return fs, cd


def save_file(line, fs, cd):
    # keep only the digits in line and turn them into ints
    line = int("".join([x for x in line if x.isdigit()]))


    if fs[cd].isnull().sum() == 0:
        # create a new row empty row
        fs.loc[len(fs)] = np.nan
    fs.loc[fs[cd].isnull().idxmax(), cd] = line


def save_directory(line, fs, cd):
    # if the column is full create a new row
    if fs[cd].isnull().sum() == 0:
        fs.loc[len(fs)] = np.nan
    # save the line in only in the first empty cell in the column cd
    fs.loc[fs[cd].isnull().idxmax(), cd] = line
    return fs


def change_directory(line, fs, cd):
    if line == "..":
        pass
    else:
        # create a new column in the dataframe and fill it with nans
        fs[line] = np.nan
        cd = line
    return fs, cd


def list_content():
    pass

def calculate_sizes(fs):
    # create a new datafram with the same columns as fs and fill it with 1 row of zeros
    sizes = pd.DataFrame(np.zeros((1, len(fs.columns))), columns=fs.columns)

    for i in range(len(fs)):
        for j in range(len(fs.columns)):
            # if the cell contains a number add it to the size of the column
            if isinstance(fs.iloc[i, j], int):
                sizes.iloc[0, j] += fs.iloc[i, j]



    print(sizes)
    print(fs)





calculate_sizes(data_prep())