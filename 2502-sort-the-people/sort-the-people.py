class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        max_hgt = max(heights)
        count_arr = [0] * (max_hgt + 1)
        
        for h in heights:
            count_arr[h] += 1
            
        for i in range(1,max_hgt + 1):
            count_arr[i] += count_arr[i - 1]
        
        output_names = [0] * n
        output_heights = [0] * n
        
        i = n - 1
        
        while(i >= 0):
            h = heights[i]
            pos = count_arr[h] - 1
            output_heights[pos] = h
            output_names[pos] = names[i]
            count_arr[h] -= 1
            i -= 1
        output_names.reverse()
        return output_names