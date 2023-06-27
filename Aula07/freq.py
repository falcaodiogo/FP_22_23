dict = {}
count = 0

with open("lus.txt", "r") as file:
    for line in file:
        for word in line:
            for letter in word:
                if letter.isalpha() == True:
                    if letter.lower() not in dict.keys():
                        dict[letter] = 1
                        count = 1
                    elif letter.lower() in dict.keys():
                        count+=1
                        dict[letter] = count

print(dict)
