from importlib.resources import path


def imp():
    path = 'ponebook.txt'
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close()
