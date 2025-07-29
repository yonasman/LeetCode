class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        
        def is_palindrome(subs: str,l:int,r:int) -> bool:
            while l < r:
                if subs[l] != subs[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, n - 1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s,left+1,right) or is_palindrome(s,left,right-1)
            left += 1
            right -= 1
        return True
        


 
           
     
               
      

