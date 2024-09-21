class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0] * (n + 1)
        for first,last,seats in bookings:
            output[first - 1] += seats
            output[last] -= seats
        for i in range(1,len(output)):
            output[i] += output[i-1]
        return output[:n]