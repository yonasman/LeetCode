class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        long_substr = ""
        long_substr_len = 0
    
        def isNice(substring):
            char_set = set(substring)
            for c in substring:
                if c.swapcase() not in char_set:
                    return False
            return True
    
        for left in range(n):
            for right in range(left + 1,n):
                substr = s[left:right + 1]
                if isNice(substr) and right - left + 1 > long_substr_len:
                    long_substr_len = right - left + 1
                    long_substr = substr
        return long_substr
        # time complexity = O(n^3)
        # space complexity = O(n)