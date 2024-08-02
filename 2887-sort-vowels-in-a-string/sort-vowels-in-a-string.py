class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        v = "aeuioAOUIE"
        vowels = []
        
        for c in s:
            if c in v:
                vowels.append(c)
        vowels.sort()
        
        s = list(s)
        vowel_idx = 0
        for i in range(len(s)):
            if s[i] in v:
                s[i] = vowels[vowel_idx]
                vowel_idx += 1
        return "".join(s)