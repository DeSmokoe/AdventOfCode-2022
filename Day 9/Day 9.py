import pandas as pd


def readfile(puzzle=False):
    if puzzle:
        filename = "Puzzle.txt"
    else:
        filename = "Test2.txt"
    with open(filename, "r") as f:
        return f.read()


def move_head(line, head, tails, positions):
    if line.startswith("R"):
        for i in range(int(line[1:])):
            head[0] += 1
            tails = move_tails(head, tails, positions)
    elif line.startswith("L"):
        for i in range(int(line[1:])):
            head[0] -= 1
            tails = move_tails(head, tails, positions)
    elif line.startswith("U"):
        for i in range(int(line[1:])):
            head[1] += 1
            tails = move_tails(head, tails, positions)
    elif line.startswith("D"):
        for i in range(int(line[1:])):
            head[1] -= 1
            tails = move_tails(head, tails, positions)
    return head, tails


def move_tails(head, tails, positions):

    for i in range(len(tails)):
        if i == 0:
            tails[i] = move_tail(head[0], head[1], tails[i][0], tails[i][1], positions)
        else:
            tails[i] = move_tail(tails[i-1][0], tails[i-1][1], tails[i][0], tails[i][1], positions)

    positions.append((tails[len(tails)-1][0], tails[len(tails)-1][1]))
    return tails


def move_tail(x_head, y_head, x_tail, y_tail, positions):
    if x_head == x_tail + 2 and y_head >= y_tail + 1 or y_head == y_tail + 2 and x_head >= x_tail + 1:
        x_tail += 1
        y_tail += 1
    elif x_head == x_tail + 2 and y_head <= y_tail - 1 or y_head == y_tail - 2 and x_head >= x_tail + 1:
        x_tail += 1
        y_tail -= 1
    elif x_head == x_tail - 2 and y_head >= y_tail + 1 or y_head == y_tail + 2 and x_head <= x_tail - 1:
        x_tail -= 1
        y_tail += 1
    elif x_head == x_tail - 2 and y_head <= y_tail - 1 or y_head == y_tail - 2 and x_head <= x_tail - 1:
        x_tail -= 1
        y_tail -= 1
    elif x_head == x_tail + 2:
        x_tail += 1
    elif x_head == x_tail - 2:
        x_tail -= 1
    elif y_head == y_tail + 2:
        y_tail += 1
    elif y_head == y_tail - 2:
        y_tail -= 1

    return x_tail, y_tail


def calculate_unique_positions(puzzle=False):
    instructions = readfile(puzzle).splitlines()
    positions = []
    head = (0, 0)
    head = list(head)
    tails = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    tails = list(tails)

    for i in range(len(instructions)):
        line = instructions[i]
        head, tails = move_head(line, head, tails, positions)

    return len(set(positions))


print(calculate_unique_positions())
print(calculate_unique_positions(True))
