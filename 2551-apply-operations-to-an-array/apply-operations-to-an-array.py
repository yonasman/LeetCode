class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1
        p1,p2 = 0,1
        while(p2 <= n):
            if(nums[p1] == nums[p2]):
                nums[p1] *= 2
                nums[p2] = 0
                p1 += 1
                p2 += 1
            else:
                p1 += 1
                p2 += 1
                continue
        non_zero_index = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[non_zero_index],nums[i] = nums[i],nums[non_zero_index]
                non_zero_index += 1
        return nums