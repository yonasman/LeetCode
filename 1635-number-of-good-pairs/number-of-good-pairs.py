class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        numOfIdentical = 0
        for i in range(n):
            for j in range(i,n):
                if nums[i] == nums[j] and i < j:
                    numOfIdentical += 1
        return numOfIdentical