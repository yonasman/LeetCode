class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        total_cost = 0
        count = 0
        for cost in costs:
            total_cost += cost
            if(total_cost > coins):
                break
            count += 1

        return count