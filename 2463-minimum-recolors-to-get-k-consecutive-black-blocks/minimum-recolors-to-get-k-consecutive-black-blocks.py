class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_w_blk = 101
        for i in range(n - k + 1):
            current_w_blocks = 0
            for j in range(i,k + i):
                if(blocks[j] == "W"):
                    current_w_blocks += 1
            min_w_blk = min(current_w_blocks,min_w_blk)
        return min_w_blk