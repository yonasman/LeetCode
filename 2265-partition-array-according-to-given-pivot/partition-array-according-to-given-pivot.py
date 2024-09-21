class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # variables to store partitioned elements
        less = []
        equal = []
        greater = []
        # iterate over the nums array and append the respective elements
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return less + equal + greater