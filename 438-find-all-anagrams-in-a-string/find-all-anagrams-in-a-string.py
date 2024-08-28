class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        p_counter = Counter(p)
        s_counter = Counter()
        output = []
    
        for i in range(n):
            s_counter[s[i]] +=1
        
            if i >= k:
                if s_counter[s[i - k]] == 1:
                    del s_counter[s[i - k]]
                else:
                    s_counter[s[i - k]] -= 1
            if s_counter == p_counter:
                output.append(i - k + 1)
        return output
            
                