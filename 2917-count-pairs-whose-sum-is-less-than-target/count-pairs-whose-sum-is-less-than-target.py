class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i,j = 0,1
        pair_count = 0
        while i < n - 1:
            if nums[i] + nums[j] < target:
                pair_count += 1
            j += 1
            if j == n:
                i += 1
                j = i + 1
        return pair_count