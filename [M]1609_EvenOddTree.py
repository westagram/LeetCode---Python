class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # Loop through the array using zip(l,r)
        # Check if the array is arithmetic by find the gap between the first 2 num
        # Go through the whole subarray and see if the gap is the same
        retList = []
        for left,right in zip(l, r):
            retList.append(self.isArithmetic(nums[left:right+1]))
        return retList


    def isArithmetic(self, array):
        if len(array) < 3:
            return True
        sortedArray = sorted(array)
        gap = sortedArray[1] - sortedArray[0]
        for i in range(2, len(sortedArray)):
            if sortedArray[i] - sortedArray[i-1] != gap:
                return False
        return True