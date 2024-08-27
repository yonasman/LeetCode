class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_set = set(nums)
        number_of_triplets = 0
        
        for num in nums:
            if (num + diff) in num_set and (num + 2 * diff) in num_set:
                number_of_triplets += 1
        return number_of_triplets