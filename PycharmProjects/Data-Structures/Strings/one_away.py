# Cracking the coding interview: 1.5

def one_away(str1, str2):
    m = len(str1)
    n = len(str2)

    if m == n:
        return replace(str1, str2)

    if abs(m - n) == 1:
        return insert_delete(str1, str2)


def replace(str1, str2):
    one_edit_check = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if one_edit_check:
                return False
            one_edit_check = True
    return True


def insert_delete(str1, str2):
    i = 0
    j = 0
    one_insert_check = False
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if one_insert_check:
                return False
            one_insert_check = True
            if len(str1) > len(str2):
                i += 1
            else:
                j += 1
        else:
            i += 1
            j += 1
    return True


str1 = "pale"
str2 = "ple"

print(one_away(str1, str2))
