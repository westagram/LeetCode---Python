class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Greedy Alg - keep buying the cheapest until has no money
        total = 0
        costs.sort()
        for ic in costs:
            if coins >= ic:
                coins -= ic
                total += 1
            else:
                break
        return total