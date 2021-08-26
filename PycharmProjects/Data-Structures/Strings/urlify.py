# Cracking the coding interview: 1.3


def urlify(str, length):
    spacecount = 0
    new_arr = list(str)
    for i in range(length):
        if str[i] == " ":
            spacecount += 1

    index = spacecount*2 + length

    for i in range(length-1,-1,-1):
        if new_arr[i] == " ":
            new_arr[index-1] = "0"
            new_arr[index-2] = "2"
            new_arr[index-3] = "%"
            index -= 3

        else:
            new_arr[index-1] = new_arr[i]
            index -= 1
    return ''.join(new_arr)

s = "Mr John Smith      "
length = 13
print(urlify(s,length))


"""
Notes: As the string is immutable in Python, it needs to be converted into a list first
"""