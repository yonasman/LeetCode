class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        min_val = min(nums)
        max_val = max(nums)
        range_val = max_val - min_val + 1
        count = [0] * range_val
    
        # Count the occurrences of each number
        for num in nums:  
            count[num - min_val] += 1
    
        # Update the count array to store the cumulative counts
        for i in range(1, range_val):
            count[i] += count[i - 1]
    
        sorted_arr = [0] * n
    
        # Place the elements in sorted order
        for j in range(n):
            index = count[nums[j] - min_val] - 1  # Subtract 1 for zero-based index
            sorted_arr[index] = nums[j]
            count[nums[j] - min_val] -= 1
        output = []
        for i in range(n):
            if sorted_arr[i] == target:
                output.append(i)
        return output