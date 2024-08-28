class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        longest_nice_str = ""
        nice_str_len = 0
        
        def isNice(sub_str):
            char_set = set(sub_str)
            
            for c in sub_str:
                if c.swapcase() not in char_set:
                    return False
            return True
        
        for start in range(n):
            for end in range(start,n):
                sub_string = s[start:end + 1]
                if isNice(sub_string) and end - start + 1 > nice_str_len:
                    nice_str_len = end - start + 1
                    longest_nice_str = sub_string
        return longest_nice_str