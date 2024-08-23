class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        n = len(nums)
        output = []
        
        for num in nums:
            output.append(sortedNums.index(num))
        return output