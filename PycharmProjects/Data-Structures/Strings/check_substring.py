# Check if s1 is a substring of s2
def isSubstring(s1, s2):
    M = len(s1)
    N = len(s2)

    for i in range(N - M + 1):
        for j in range(M):
            if s2[i + j] != s1[j]:
                break
            if j + 1 == M:
                return i
    return -1


s1 = "for"
s2 = "geeksforgeeks"
print(isSubstring(s1, s2))

# M = 3
# N = 13
# range(11)
