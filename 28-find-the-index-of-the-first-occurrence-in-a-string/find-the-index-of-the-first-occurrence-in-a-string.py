class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0, len(needle)
        n = len(haystack)
        while p1 < n:
            if haystack[p1:p2] == needle:
                return p1
            else:
                p1 += 1
                p2 += 1
        return -1