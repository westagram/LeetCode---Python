class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sortedPile = sorted(piles)
        totalAdd = len(sortedPile) // 3
        total, ans, n = len(sortedPile), 0, 2
        for _ in range(totalAdd):
            ans += sortedPile[total - n]
            n += 2
        return ans
