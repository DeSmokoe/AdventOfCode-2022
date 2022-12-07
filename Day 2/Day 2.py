import numpy as np

def read_input(filename):
    with open(filename, "r") as f:
        return f.read()

def dataprep(data):
    my_file = read_input(data)
    array = my_file.split("\n")
    # turn strings into chars
    array = [list(x) for x in array]
    # remove empty chars in the list in the array
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == " ":
                array[i].remove(array[i][j])
                break

    return array


def calculate_score_part1(array):
    score = 0

    for i in range(len(array)):
        if array[i][1] == "X" and array[i][0] == "A":
            score += 4
        elif array[i][1] == "X" and array[i][0] == "B":
            score += 1
        elif array[i][1] == "X" and array[i][0] == "C":
            score += 7
        elif array[i][1] == "Y" and array[i][0] == "A":
            score += 8
        elif array[i][1] == "Y" and array[i][0] == "B":
            score += 5
        elif array[i][1] == "Y" and array[i][0] == "C":
            score += 2
        elif array[i][1] == "Z" and array[i][0] == "A":
            score += 3
        elif array[i][1] == "Z" and array[i][0] == "B":
            score += 9
        elif array[i][1] == "Z" and array[i][0] == "C":
            score += 6

    return score


def calculate_score_part2(array):
    score = 0

    for i in range(len(array)):
        if array[i][1] == "X" and array[i][0] == "A":
            score += 3
        elif array[i][1] == "X" and array[i][0] == "B":
            score += 1
        elif array[i][1] == "X" and array[i][0] == "C":
            score += 2
        elif array[i][1] == "Y" and array[i][0] == "A":
            score += 4
        elif array[i][1] == "Y" and array[i][0] == "B":
            score += 5
        elif array[i][1] == "Y" and array[i][0] == "C":
            score += 6
        elif array[i][1] == "Z" and array[i][0] == "A":
            score += 8
        elif array[i][1] == "Z" and array[i][0] == "B":
            score += 9
        elif array[i][1] == "Z" and array[i][0] == "C":
            score += 7

    return score


print(calculate_score_part1(dataprep("Test Input.txt")))
print(calculate_score_part1(dataprep("Puzzle Input.txt")))

print(calculate_score_part2(dataprep("Test Input.txt")))
print(calculate_score_part2(dataprep("Puzzle Input.txt")))

