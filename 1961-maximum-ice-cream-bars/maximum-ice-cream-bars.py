class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        num_of_ice_creams = 0
        for c in costs:
            if c <= coins:
                num_of_ice_creams += 1
                coins -= c
            elif c > coins or coins == 0:
                break
        return num_of_ice_creams