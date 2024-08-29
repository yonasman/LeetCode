class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        max_length = 0
        num_of_zeros = 0
    
        for right in range(n):
            if nums[right] == 0:
                num_of_zeros += 1
            while num_of_zeros > 1:
                if nums[left] == 0:
                    num_of_zeros -= 1
                left += 1
            max_length = max(max_length, right - left)
        return max_length