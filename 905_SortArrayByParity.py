class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        eList, oList = [],[]
        for n in A:
            eList.append(n) if n%2 == 0 else oList.append(n)
        return eList + oList
