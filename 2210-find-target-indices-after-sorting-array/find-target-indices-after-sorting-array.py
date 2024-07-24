class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        new_arr = []
        for i in range(n):
            if(nums[i] == target):
                new_arr.append(i)
        return new_arr