class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count_of_ice_creams = 0
        cost_of_ice_creams = 0
    
        for cost in costs:
            if cost_of_ice_creams + cost <= coins:
                cost_of_ice_creams += cost
                count_of_ice_creams += 1
        return count_of_ice_creams