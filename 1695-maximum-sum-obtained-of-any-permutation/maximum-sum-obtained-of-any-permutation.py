class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * n
    
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        for i in range(1, n):
            freq[i] += freq[i - 1]

        nums.sort()
        freq.sort()

        total_sum = 0
        for i in range(n):
            total_sum = (total_sum + nums[i] * freq[i]) % MOD

        return total_sum