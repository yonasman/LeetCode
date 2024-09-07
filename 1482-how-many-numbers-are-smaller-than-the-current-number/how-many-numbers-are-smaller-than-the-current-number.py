class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        
        for n in nums:
            d[n] = d.get(n,0) + 1
            
        sortedNums = sorted(d.keys())
        
        cummulative_sum = 0
        cummulative_count = {}
        
        for num in sortedNums:
            cummulative_count[num] = cummulative_sum
            cummulative_sum += d[num]
        # output
        output = [cummulative_count[n] for n in nums]
        return output
            