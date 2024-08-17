class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[non_zero_idx] = nums[non_zero_idx],nums[i]
                non_zero_idx += 1
        # time complexity = O(n)
        # space complexity = O(1)