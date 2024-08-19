class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n // 2] 
        # time complexity = O(nlogn)
        # space complexity = O(n)