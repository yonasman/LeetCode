class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[p1],nums[i] = nums[i],nums[p1]
                p1 += 1
        return nums