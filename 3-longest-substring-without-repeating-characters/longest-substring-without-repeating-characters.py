class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start = 0
        char_set = set()
        max_length = 0
        
        for end in range(n):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        return max_length