# Cracking the coding interview: 1.3


def urlift(str, truelength):

    spacecount  = 0

    for i in str:
        if i == " ":
            spacecount+=1
    index = truelength + spacecount * 2
    str = "Mr John Smith    "
    strlist = list(str)

    for i in range(truelength-1,-1,-1):
        if strlist[i] == " ":
           strlist[index-3] = "%"
           strlist[index - 2] = "2"
           strlist[index - 1] = "0"
           index = index -3
        else:
            strlist[index-1] = strlist[i]
            index -=1
    return "".join(strlist)


str = "Mr John Smith"
print(urlift(str,13))