class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        n = len(nums)
        output = []
        for i in range(n):
            print(sortedNums[:nums[i]])
            output.append(len(sortedNums[:sortedNums.index(nums[i])]))
        return output