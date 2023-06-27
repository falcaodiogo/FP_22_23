def ispalindrome(s):
    result = "Palídrome"
    for i in range(len(s)//2):
        if s[i] == s[len(s)-1-i]:
            continue
        else:
            result = "Não palíndrome"
            break
    return result

print(ispalindrome("badab"))