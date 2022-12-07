def readfile(filename):
    my_file = open(filename, "r")
    return my_file.read()


my_file = readfile("Test Input.txt")
array = my_file.split("\n")

for i in range(len(array)):
    if array[i] == "":
        array[i] = 0
    else:
        array[i] = int(array[i])


print(array)
