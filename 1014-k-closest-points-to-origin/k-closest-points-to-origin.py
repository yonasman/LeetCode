import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)
        
        sortedPoints = sorted(points, key=distance_from_origin)
        return sortedPoints[:k]