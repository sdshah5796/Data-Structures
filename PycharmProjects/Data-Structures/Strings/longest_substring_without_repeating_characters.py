# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# https://www.youtube.com/watch?v=3IETreEybaA&ab_channel=NickWhite

def lengthOfLongestSubstring(s):
    dict = {}
    count = 0
    start = 0
    i = 0
    while i < len(s):
        if s[i] in dict:
            dict.pop(s[start])

            start += 1

        else:
            dict[s[i]] = 1
            i += 1
            count = max(count, len(dict))
    return count

# pwwkew