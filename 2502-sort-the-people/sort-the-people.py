class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        max_ht = max(heights)
        count = [0] * (max_ht + 1)
        
        for h in heights:
            count[h] += 1
        for i in range(1, max_ht + 1):
            count[i] += count[i - 1]
        
        outputHeights = [0] * n
        outputNames = [0] * n
        
        for i in range(n - 1, -1,-1):
            height = heights[i]
            name = names[i]
            
            position = count[height] - 1
            outputHeights[position] = height
            outputNames[position] = name
            
            # decrease the count at height
            count[height] -= 1
        outputNames.reverse()
        return outputNames