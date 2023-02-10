class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinctSet = set(nums)
        if len(distinctSet) < 3:
            return max(distinctSet)
        for _ in range(2):
            distinctSet.remove(max(distinctSet))
        return max(distinctSet)
