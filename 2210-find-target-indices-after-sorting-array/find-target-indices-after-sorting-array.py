class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        output = []
        
        for i in range(n):
            if nums[i] == target:
                output.append(i)
        return output