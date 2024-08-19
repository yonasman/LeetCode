class Solution:
    def repeatedCharacter(self, s: str) -> str:
        n = len(s)
        idx = float("inf")
        for i in range(n):
            for j in range(i + 1,n):
                if s[i] == s[j]:
                    idx = min(idx, j)
        return s[idx]