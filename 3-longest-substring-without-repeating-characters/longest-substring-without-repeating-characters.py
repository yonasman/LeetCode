class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        left = 0
        right = 0
        maxLen = 0
        seen = set()
        while left < n and right < n:
            if s[right] not in seen:
                seen.add(s[right])
                maxLen = max(maxLen, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return maxLen    
            