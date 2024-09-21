class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        # build prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        # building the suffix products and compute the final answer
        suffix = 1
        for j in range(n-1,-1,-1):
            output[j] *= suffix
            suffix *= nums[j]
        return output