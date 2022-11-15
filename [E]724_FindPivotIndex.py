class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for idx, n in enumerate(nums):
            rightSum -= n
            if leftSum == rightSum:
                return idx
            leftSum += n
        return -1