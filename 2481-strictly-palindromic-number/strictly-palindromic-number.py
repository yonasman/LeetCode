class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2,n-1):
            str_bin = ""
            num = n
            while num:
                str_bin = str(num % base) + str_bin
                num = num // base
            if(str_bin != str_bin[::-1]):
                return False
        return True