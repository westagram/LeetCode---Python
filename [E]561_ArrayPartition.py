class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sumList = []
        nums.sort()
        for idx in range(0, len(nums), 2):
            sumList.append(min(nums[idx], nums[idx+1]))
        return sum(sumList)