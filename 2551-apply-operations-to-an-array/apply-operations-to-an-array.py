class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i - 1]:
                nums[i] = 0
                nums[i - 1] *=2
        p1 = 0
        for i in range(n):
            if nums[i] != 0:
                nums[p1],nums[i] = nums[i],nums[p1]
                p1 += 1
        return nums