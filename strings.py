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
