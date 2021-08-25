# Cracking the coding interview: 1.4

def pallindrome_permutation(str):
    letter_count = [0] * 128

    for i in str:
        letter_count[ord(i)] +=1

    count = 0
    for i in letter_count:
        count += i%2

    return count <=1

str ="abbc"
print(pallindrome_permutation(str))