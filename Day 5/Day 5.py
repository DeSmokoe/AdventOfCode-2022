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

    # keep only the digits in table2 and turn them into ints
    table2 = table2.applymap(lambda x: int("".join([y for y in x if y.isdigit()])))

    table2["Amount"] = table2[0].apply(lambda x: int(str(x)[:len(str(x)) // 2]))
    table2["Origin"] = table2[0].apply(lambda x: int(str(x)[len(str(x)) - 2]))
    table2["Destination"] = table2[0].apply(lambda x: int(str(x)[len(str(x)) - 1]))
    table2 = table2.iloc[:, 1:]


    print(table1, table2)




dataprep("Test.txt")