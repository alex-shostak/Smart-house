import os

file_name = "log.txt"


def remove():
    try:
        os.remove(file_name)
    except:
        pass


def write(message):
    with open(file_name, 'a') as f:
        print(message, file=f)
