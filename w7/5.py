import os

def printContent(level, path):
    for x in os.listdir(path):
        for i in range(level + 1):
            print('-----',end='')
        print(x)
        if os.path.isdir(path + "/" + x):
            printContent(level + 1, path + "/" + x)


printContent(0, ".")