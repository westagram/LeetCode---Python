class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)
        returnList = []
        for num in candies:
            if num + extraCandies >= greatest:
                returnList.append(True)
            else:
                returnList.append(False)
        return returnList
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
