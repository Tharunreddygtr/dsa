def lengthOfLongestSubstring(s):
    if not s:
        return 0
    if len(set(s)) == len(s):
        return len(s)
    left = 0
    right = 0
    dict1 = {}
    ans = 0
    while left < len(s) and right < len(s):
        if s[right] not in dict1:
            dict1[s[right]] = 1
            right += 1
            ans = max(ans, right - left)
        else:
            while s[right] in dict1:
                del dict1[s[left]]
                left += 1
    return ans


s = "abcabcbb"
print(lengthOfLongestSubstring(s))


def characterReplacement(s, k):
    c_frequency = {}
    max_str = 0
    left = 0
    right = 0
    while left < len(s) and right < len(s):
        if not s[right] in c_frequency:
            c_frequency[s[right]] = 0
        c_frequency[s[right]] += 1
        cells_count = right - left + 1
        if cells_count - max(c_frequency.values()) <= k:
            max_str = max(max_str, cells_count)
            right += 1
        else:
            c_frequency[s[left]] -= 1
            left += 1
            right += 1

    return max_str


s = "AABABBA"
k = 1
print(characterReplacement(s, k))

def zig_zag_convert(s, numRows):
    if numRows == 1:
        return s
    list1 = [""]*numRows
    current = 0
    move_down = True
    i = 0
    while i < len(s):
        list1[current] += s[i]
        if move_down:
            current += 1
        else:
            current -= 1
        if current + 1 == numRows:
            move_down = False
        if current == 0:
            move_down = True
        i+=1
    return "".join(list1)
s = "PAYPALISHIRING"
numRows = 3
print(zig_zag_convert(s, numRows))
