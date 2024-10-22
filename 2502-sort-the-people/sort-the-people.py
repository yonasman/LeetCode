class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if heights[j] < heights[j + 1]:
                    swapped = True
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    names[j],names[j+1] = names[j+1],names[j]
            if not swapped:
                return names
        return names