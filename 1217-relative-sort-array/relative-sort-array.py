
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        # array to store unique elements of arr1
        unique = []
        # count the freq of number in arr1
        freq = {}
        for num in arr1:
            freq[num] = freq.get(num,0) + 1
        # result array
        result = []
        # sort the common elements using arr2
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]
        for num,count in freq.items():
            unique.extend([num] * count)
        # sort the remaining elements
        remaining_ele = sorted(unique)
        result.extend(remaining_ele)
        return result