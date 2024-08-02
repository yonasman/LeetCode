class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if(nums[j] < nums[min_idx]):
                    nums[min_idx],nums[j] = nums[j], nums[min_idx]
        output = []
        for i in range(0,n,2):
            if i + 1 < n:
                a = nums[i]
                b = nums[i + 1]
                output.append(b)
                output.append(a)
        return output