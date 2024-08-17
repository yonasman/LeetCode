class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] > nums[j]:
                    count += 1
            output.append(count)
        return output