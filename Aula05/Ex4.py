def allMatches(list):
    matches = []
    if len(list) == 0:
        return []
    if len(list) == 1:
        return list
    else:
        for i in range(len(list)):
            for j in range(i+1, len(list)):
                matches.append([list[i], list[j]])
        return matches