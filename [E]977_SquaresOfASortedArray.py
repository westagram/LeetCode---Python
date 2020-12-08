class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ### 2 pointers method
        if A[0] >= 0:
            return [i**2 for i in A]
        
        negIdx = 0
        for idx in range(len(A)):
            if A[idx] <= 0:
                negIdx = idx
        
        count = 0
        returnList = []
        posIdx = negIdx + 1
        while count != len(A):
            if posIdx == len(A) or A[negIdx]**2 < A[posIdx]**2:
                returnList.append(A[negIdx]**2)
                negIdx -= 1
            else:
                returnList.append(A[posIdx]**2)
                posIdx += 1
            count += 1
            
        return returnList
                