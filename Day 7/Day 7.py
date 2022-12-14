import pandas as pd
import numpy as np

# Create a DirectoryNode class
class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent


def readfile(puzzle=False):
    if puzzle:
        filename = "Puzzle.txt"
    else:
        filename = "Test.txt"
    with open(filename, "r") as f:
        return f.read()


def data_prep(puzzle=False):
    terminal_output = readfile(puzzle).splitlines()
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
    # Keep only the digits in the line
    line = "".join([x for x in line if x.isdigit()])

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
        # add line as a child object to the root
        root.add_child(DirectoryNode(line))


        # create a new column in the dataframe and fill it with nans
        fs[line] = np.nan
        cd = line
    return fs, cd


def list_content():
    pass

def calculate_folder(fs):
    # create a new dataframe with the same columns as fs and fill it with 1 row of zeros
    sizes = pd.DataFrame(np.zeros((1, len(fs.columns))), columns=fs.columns)

    for i in range(len(fs)):
        for j in range(len(fs.columns)):
            # if the cell contains a number add it to the size of the column
            if isinstance(fs.iloc[i, j], str) and fs.iloc[i, j].isdigit():
                sizes.iloc[0, j] += int(fs.iloc[i, j])

    for i in range(len(fs)):
        for j in range(len(fs.columns)-1, -1, -1):
            # if the cell contains a string add the size of the column corresponding to the string
            if isinstance(fs.iloc[i, j], str) and not fs.iloc[i, j].isdigit():
                sizes.iloc[0, j] += sizes.iloc[0, fs.columns.get_loc(fs.iloc[i, j])]

    # turn the sizes into integers and put them in a list
    sizes = sizes.astype(int).values.tolist()[0]

    return sizes


def calculate_total(sizes):

    # calculate the sum of all the ints smaller than 100000
    total = sum([x for x in sizes if x < 100000])

    # get children of root and print their names
    children = root.get_children()
    for child in children:
        print(child.name)

    print(total)


root = DirectoryNode("root")

calculate_total(calculate_folder(data_prep()))
# calculate_total(calculate_folder(data_prep(puzzle=True)))
