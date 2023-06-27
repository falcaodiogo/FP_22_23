import os


def tam(file, dir):
    if os.path.exists(dir) == True:
        with open(file, "r") as f:
            return os.stat(file).st_size