class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Make a set so search runtime is shorter
        # Create a dict to keep track of how many nums ahead
        # Go through set, and see if there's a higher num

        inputSet = set(nums)
        total = 0
        for num in inputSet:
            if num - 1 not in inputSet: # IMPORTANT HERE
                tempTotal = 1
                tempNum = num
                while tempNum + 1 in inputSet:
                    tempNum += 1
                    tempTotal += 1
                total = max(total, tempTotal)
        return total