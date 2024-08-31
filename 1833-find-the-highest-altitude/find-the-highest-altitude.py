class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        altitude = [0] * (n + 1)
        altitude[0] = 0
        altitude[1] = gain[0]
    
        for i in range(2,n + 1):
            altitude[i] = altitude[i - 1] + gain[i - 1]
        return max(altitude)