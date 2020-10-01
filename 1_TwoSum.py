class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        masterDict = dict() #val:idx
        # print(nums)
        # print(target)
        for i in range(len(nums)):
            if target - nums[i] in masterDict:
                return[masterDict[target - nums[i]], i]
            masterDict[nums[i]] = i
        return []
            
