class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newList = []
        addOne = True
        for i in range(len(digits)):
            curDigit = digits[-1-i]
            if addOne:
                curDigit += 1
            if curDigit > 9:
                newList.append(0)
            else:
                newList.append(curDigit)
                addOne = False
        if addOne:
            newList.append(1)
        return newList[::-1]
