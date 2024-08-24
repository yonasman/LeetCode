class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        num_of_ice_creams = 0
        current_cost = 0
        for cost in costs:
            if current_cost + cost <= coins:
                current_cost += cost
                num_of_ice_creams += 1
        return num_of_ice_creams