class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zero_idx = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1
        for j in range(non_zero_idx,n):
            nums[j] = 0
        # time complexity = O(n)
        # space complexity = O(1)