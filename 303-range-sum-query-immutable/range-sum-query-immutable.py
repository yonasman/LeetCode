class NumArray:

    def __init__(self, nums: List[int]):
        
        n = len(nums)
        self.prefix_sum = [0] * n
        self.prefix_sum[0] = nums[0]
        
        for i in range(1,n):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]  
        print(self.prefix_sum)
    
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)