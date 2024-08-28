class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = sum(nums[:k])
        max_avg = current_sum / k
        
        for j in range(k,n):
            current_sum += nums[j] - nums[j - k]
            max_avg = max(current_sum / k, max_avg)
        return max_avg