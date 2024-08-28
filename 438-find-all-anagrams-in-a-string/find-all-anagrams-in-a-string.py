class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        n = len(s)
        i = 0
        j = i + len(p)
        output = []
        
        while j <= n:
            if sorted(s[i:j]) == p:
                output.append(i)
            j += 1
            i += 1
        return output
            
                