class Solution(object):
    def runningSum(self, nums):
        totalSum = 0
        resultList = []
        for num in nums:
            totalSum += num
            resultList.append(totalSum)
        return resultList
        """
        :type nums: List[int]
        :rtype: List[int]
        """
