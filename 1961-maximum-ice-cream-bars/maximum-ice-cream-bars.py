class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
            n = len(costs)
    
            count_arr = [0] * (max(costs) + 1)
    
            for cost in costs:
                count_arr[cost] += 1
            for i in range(1,max(costs) + 1):
                count_arr[i] += count_arr[i - 1]
    
            sortedCosts = [0] * n
            for i in range(n - 1,-1,-1):
                cost = costs[i]
                position = count_arr[cost] - 1
                sortedCosts[position] = cost
                count_arr[cost] -= 1
            num_of_ice_cream = 0
            current_cost = 0
            for cost in sortedCosts:
                if current_cost + cost <= coins:
                    current_cost += cost
                    num_of_ice_cream += 1

            return num_of_ice_cream