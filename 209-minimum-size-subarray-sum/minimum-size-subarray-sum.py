class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        start = 0
        min_length = float("inf")
        current_sum = 0
        
        for end in range(n):
            current_sum += nums[end] 
            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1
        return min_length if min_length != float("inf") else 0