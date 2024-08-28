class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        max_avg = float("-inf")
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        for j in range(k,n+1):
            current_sum = prefix_sum[j] - prefix_sum[j - k]
            max_avg = max(max_avg, current_sum / k)
        return max_avg