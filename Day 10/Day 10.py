def readfile(puzzle=False):
    if puzzle:
        filename = "Puzzle.txt"
    else:
        filename = "Test.txt"
    with open(filename, "r") as f:
        return f.read()


def cycle(line, register):
    # if line starts with "noop" then do nothing
    if line[:4] == "noop":
        noop(register)
    elif line[:4] == "addx":
        value = int(line[4:])
        addx(register, value)


def run(puzzle=False):
    instructions = readfile(puzzle).splitlines()
    register = [1]

    for line in instructions:
        cycle(line, register)

    calculate_signal_strength(register)


def noop(register):
    register.append(register[-1])


def addx(register, value):
    register.append(register[-1])
    register.append(register[-1] + value)


def calculate_signal_strength(register):
    signal_strength = 0
    for i in range(20, len(register), 40):
        signal_strength += register[i]*i
        print(i, register[i])
    print(signal_strength)


run()