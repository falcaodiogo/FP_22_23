def compareFiles(file1, file2):
    with open(file1, "wb") as f1:
        with open(file2, "wb") as f2:
            for line1, line2 in f1, f2:
                if line1 != line2:
                    return False
                    break
                else:
                    continue
    return True