class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 1
        
        while i < n:
            nums[i] = nums[i - 1] + nums[i]
            i += 1
        return nums