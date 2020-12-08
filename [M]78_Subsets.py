import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        returnList = [[]]
        for num in nums:
            tempReturnList = copy.deepcopy(returnList)
            for item in tempReturnList:
                temp = copy.deepcopy(item)
                temp.append(num)
                returnList.append(temp)
        return returnList