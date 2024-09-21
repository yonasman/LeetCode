class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        output = [0] * n
        left = 0
        # build the less elements
        for num in nums:
            if num < pivot:
                output[left] = num
                left += 1
        # build the equal elements
        for num in nums:
            if num == pivot:
                output[left] = num
                left += 1
        # buld the greate elements
        for num in nums:
            if num > pivot:
                output[left] = num
                left += 1
        return output