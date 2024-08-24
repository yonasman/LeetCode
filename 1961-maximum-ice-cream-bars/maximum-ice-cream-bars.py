class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        num_of_ice_creams = 0
        costs.sort()
        for c in costs:
            if c <= coins:
                num_of_ice_creams += 1
                coins -= c
        return num_of_ice_creams