class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumNums = sum(nums)
        sumAllNums = sum([i for i in range(len(nums)+1)])
        return sumAllNums - sumNums