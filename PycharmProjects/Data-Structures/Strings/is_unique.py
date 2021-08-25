# Cracking the coding interview: 1.1


def is_unique(string):
    if len(string) > 256:
        return False
    char_set = [False]*256

    for i in range(len(string)):
        value = ord(string[i])

        if char_set[value] == True:
            return False
        char_set[value] = True

    return True


# Only valid for a-z
def is_unique_bit_manipulation(str):
    checker = 0

    for i in range(len(str)):
        bitAtIndex = ord(str[i]) - ord('a')
        print(bitAtIndex)

        # If that bit is already set in
        # checker, return False
        if (bitAtIndex) > 0:
            if (checker & ((1 << bitAtIndex))) > 0:
                return False

            # Otherwise update and continue by
            # setting that bit in the checker
            checker = checker | (1 << bitAtIndex)

    # No duplicates encountered, return True
    return True



st = "ABCA"
print(is_unique(st))
print(is_unique_bit_manipulation(st))
