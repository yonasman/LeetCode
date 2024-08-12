class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # dictionary to count the number of unique items
        d = {}
        numOfIdentical = 0
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for value in d.values():
            if value > 1:
                numOfIdentical += (value * (value - 1)) // 2
        return numOfIdentical
        # time complexity O(n)
        # space complexity O(n)