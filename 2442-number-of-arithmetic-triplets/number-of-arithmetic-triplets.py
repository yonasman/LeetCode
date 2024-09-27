class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        numOfTriplets = 0
        for num in nums:
            if (num - diff) in nums and (num + diff) in nums:
                numOfTriplets += 1
        return numOfTriplets