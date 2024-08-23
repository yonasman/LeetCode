class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNums = "abcdefghijklmnopqrstuvwxyz1234567890"
        s = s.lower()
        newStr = ""
        
        for c in s:
            if c in alphaNums:
                newStr += c
        return newStr == newStr[::-1]