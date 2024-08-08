class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            temp_num = n
            str_bin = ""
            while temp_num:
                str_bin = str(temp_num % i) + str_bin
                temp_num = temp_num // i
            if str_bin != str_bin[::-1]:
                return False
        return True