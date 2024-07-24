class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        new_arr = []
        
        for i in range(0,n,2):
            if i + 1 < n:
                A = nums[i]
                B = nums[i+1]
                new_arr.append(B)
                new_arr.append(A)
        return new_arr