# Cracking the coding interview: 1.2

# Can be done through sorting and comparing the strings

def permutation_of_other(string1, string2):
    if len(string1) != len(string2):
        return False

    count = [0 for i in range(256)]

    for i in range(len(string1)):
        count[ord(string1[i])] += 1
        count[ord(string2[i])] -= 1

    for i in range(256):
        if count[i]:
            return False
    return True




string1 = "abcd"
string2 = "bcde"
print(permutation_of_other(string1, string2))
