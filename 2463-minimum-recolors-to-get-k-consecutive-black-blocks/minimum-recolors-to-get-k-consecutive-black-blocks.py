class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_operations = float("inf")
        
        for i in range(n - k + 1):
            sub_block = blocks[i:k+i]
            min_operations = min(min_operations, sub_block.count("W"))
        return min_operations