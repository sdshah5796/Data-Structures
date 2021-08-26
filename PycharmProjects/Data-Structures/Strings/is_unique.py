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

'''
Notes:
Ask the interviewer if it's a unicode string or an ASCII string
Time complexity: O(c) or o(n) where c is the size of the character set
Space complexity: O(c)

If we can't use additional data structures, we can do the following:
1. Compare every character of the string to every other character of the string. This will take 0( n^2) time
and 0(1) space.

2. If we are allowed to modify the input string, we could sort the string in O(nlog(n)) time and then
linearly check the string for neighboring characters that are identical. Careful, though: many sorting
algorithms take up extra space.
'''
