class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # variable to store the max harmonious length
        maxHarmoniousLen = 0
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        # iterate over nums and keep track of the max len
        for num in nums:
            if num + 1 in hashMap:
                maxHarmoniousLen = max(maxHarmoniousLen, hashMap[num] + hashMap[num + 1])
        return maxHarmoniousLen
    