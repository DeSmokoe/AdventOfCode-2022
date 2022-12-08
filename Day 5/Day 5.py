import pandas as pd


def readfile(filename):
    with open(filename, "r") as f:
        return f.read()


def dataprep(data):
    my_file = readfile(data)

    # make a table with the data
    table = pd.DataFrame([x.split(",") for x in my_file.split("\n")])

    # find the index of the empty line
    empty_line = table[table[0] == ""].index[0]

    # split the table into two tables seperated by the empty line
    table1 = table.iloc[:empty_line]
    table2 = table.iloc[empty_line + 1:]

    # turn the strings into chars in table1
    table1 = table1.applymap(lambda x: list(x))

    # turn every char in table1 in a new column
    table1 = table1.apply(lambda x: pd.Series(x[0]), axis=1)

    # keep only every fourth column, starting from the second column in table1
    table1 = table1.iloc[:, 1::4]

    # rename the columns in table1 to ascending numbers starting from 1
    table1.columns = range(1, len(table1.columns) + 1)

    # remove the last row in table1
    table1 = table1.iloc[:-1]

    # keep only the digits in table2 and turn them into ints
    table2 = table2.applymap(lambda x: int("".join([y for y in x if y.isdigit()])))

    table2["Amount"] = table2[0].apply(lambda x: int(str(x)[:len(str(x)) // 2]))
    table2["Origin"] = table2[0].apply(lambda x: int(str(x)[len(str(x)) - 2]))
    table2["Destination"] = table2[0].apply(lambda x: int(str(x)[len(str(x)) - 1]))
    table2 = table2.iloc[:, 1:]

    # rename the rows in table2 to ascending numbers starting from 0
    table2.index = range(len(table2))

    return table1, table2


def move_crates(position, instructions, type_crane):
    # For each instruction
    for i in range(len(instructions)):
        # for the right amount of crates

        dest_col = instructions["Destination"][i]
        ori_col = instructions["Origin"][i]
        if type_crane == "9001":
            ori_row_safe = len(position) - len(position[position[ori_col] != " "])

        for j in range(instructions["Amount"][i]):
            # Declarations
            dest_row = len(position)-len(position[position[dest_col] != " "]) - 1

            if type_crane == "9000":
                ori_row = len(position)-len(position[position[ori_col] != " "])
            elif type_crane == "9001":
                ori_row = ori_row_safe + instructions["Amount"][i] - j - 1

            if dest_row == -1:
                dest_row += 1
                ori_row += 1
                if type_crane == "9001":
                    ori_row_safe += 1

                # Create a new row at the top of the table
                position.loc[-1] = [" "] * len(position.columns)
                position.index = position.index + 1
                position = position.sort_index()

            # Move to new position
            position[dest_col][dest_row] = position[ori_col][ori_row]
            # Remove original
            position[ori_col][ori_row] = " "

    return position


def find_top_crates(position):

    # find the first not empty characters in the top of each column
    top_crates = position.apply(lambda x: x[x != " "].iloc[0], axis=0)

    # write the characters in a string
    top_crates = "".join(top_crates)

    print(top_crates)


find_top_crates(move_crates(dataprep("Test.txt")[0], dataprep("Test.txt")[1], "9000"))
find_top_crates(move_crates(dataprep("Puzzle.txt")[0], dataprep("Puzzle.txt")[1], "9000"))
find_top_crates(move_crates(dataprep("Test.txt")[0], dataprep("Test.txt")[1], "9001"))
find_top_crates(move_crates(dataprep("Puzzle.txt")[0], dataprep("Puzzle.txt")[1], "9001"))
