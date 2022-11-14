class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinHelper(nums)
    
    def findMinHelper(self, nums):
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]

        high = len(nums) - 1
        low = 0
        mid = len(nums)//2
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        if nums[high] < nums[mid]:
            return self.findMinHelper(nums[mid:])
        else:
            return self.findMinHelper(nums[:mid])