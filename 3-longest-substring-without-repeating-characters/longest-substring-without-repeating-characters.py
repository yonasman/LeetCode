class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        p1 = 0
        maxLen = 0
        seen = set()
        for p2 in range(n):
            while s[p2] in seen:
                seen.remove(s[p1])
                p1 += 1
            seen.add(s[p2])
            maxLen = max(maxLen, p2 - p1 + 1)
        return maxLen