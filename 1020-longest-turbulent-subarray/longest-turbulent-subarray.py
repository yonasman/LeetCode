class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        
        max_length = 1
        start = 0
        
        for end in range(1, n):
            # Check for equal elements which break the turbulence
            if arr[end] == arr[end - 1]:
                start = end
            
            # Check if the current window is turbulent
            elif end > 1 and ((arr[end] < arr[end - 1] and arr[end - 1] > arr[end - 2]) or
                              (arr[end] > arr[end - 1] and arr[end - 1] < arr[end - 2])):
                max_length = max(max_length, end - start + 1)
            else:
                # Reset the start pointer if turbulence pattern breaks
                start = end - 1
        max_length = max(max_length, n - start)
        return max_length
