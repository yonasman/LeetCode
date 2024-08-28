class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_opr = sum(1 for i in range(k) if blocks[i] == "W")
        min_w = min_opr
        
        for j in range(k,n):
            if blocks[j - k] == "W":
                min_w -= 1
            if blocks[j] == "W":
                min_w += 1
            min_opr = min(min_opr, min_w)
        return min_opr
            