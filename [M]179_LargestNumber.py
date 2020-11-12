class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def helperComp(a,b):
            if a == b:
                return 0
            elif a+b > b+a:
                return -1
            else:
                return 1
        
        returnStringNum = ""
        strNums = [str(i) for i in nums]
        for ele in sorted(strNums, key=functools.cmp_to_key(helperComp)):
            returnStringNum += ele
        if int(returnStringNum) == 0:
            return "0"
        return returnStringNum
