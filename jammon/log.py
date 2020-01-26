import os

file_name = "log.txt"


def remove():
    try:
        os.remove(file_name)
    except:
        pass


def write(message):
    try:
        with open(file_name, 'w') as f:
            print(message, file=f)
    except:
        pass


def append(message):
    try:
        with open(file_name, 'a') as f:
            print(message, file=f)
    except:
        pass