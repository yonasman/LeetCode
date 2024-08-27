from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char_count = defaultdict(int)
        max_char_count = 0
        left = 0
        
        for right in range(n):
            char_count[s[right]] += 1
            max_char_count = max(max_char_count, char_count[s[right]])
            
            while(right -  left + 1) - max_char_count > k:
                char_count[s[left]] -= 1
                left += 1
        return n - left