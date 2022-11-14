class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        startIdx = 0
        endIdx = 1
        ret = 0
        while (endIdx < len(prices)):
            if prices[startIdx] < prices[endIdx]:
                ret = max(ret, prices[endIdx] - prices[startIdx])
            else:
                startIdx = endIdx
            endIdx += 1
        return ret