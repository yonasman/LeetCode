class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # sort the list
        points.sort()
        widest_vert_area = 0
        
        for i in range(1,len(points)):
            widest_vert_area = max(widest_vert_area, points[i][0] - points[i - 1][0])
            
        return widest_vert_area