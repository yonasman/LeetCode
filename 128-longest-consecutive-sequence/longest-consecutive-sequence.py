class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLen = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                current_num = num
                while current_num + 1 in nums_set:
                    length += 1
                    current_num += 1
                maxLen = max(maxLen, length)
        return maxLen