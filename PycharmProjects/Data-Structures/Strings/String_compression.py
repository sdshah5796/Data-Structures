# Cracking the coding interview: 1.6
# https://leetcode.com/problems/string-compression/


# This solution is done in-place as per the leetcode problem
def compress(chars):
    count = 1
    for i in range(len(chars) - 1, -1, -1):

        if i and chars[i] == chars[i - 1]:
            count += 1
            chars.pop(i)
        else:
            if count > 1:
                strint = str(count)
                j = i + 1
                for z in strint:
                    chars.insert(j,z)
                    j += 1
                count = 1


