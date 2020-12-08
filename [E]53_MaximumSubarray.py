class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        (curSum, maxSum) = (nums[0], nums[0])
        for idx in range(1, len(nums)):
            curSum = max(curSum + nums[idx], nums[idx])
            maxSum = max(curSum, maxSum)
        return maxSum