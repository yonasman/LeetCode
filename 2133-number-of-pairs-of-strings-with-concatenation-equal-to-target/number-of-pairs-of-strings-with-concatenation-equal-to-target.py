class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        num_of_pairs = 0
        for i in range(n):
            num = nums[i]
            if target.startswith(num):
                remaining = target[len(num):]
                for j in range(n):
                    if i != j and remaining == nums[j]:
                        num_of_pairs += 1
        return num_of_pairs