class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        masterList = [[] for i in range(numRows)]
        
        count = 0
        increase = True
        for i in s:
            if count == 0:
                increase = True
            elif count == numRows - 1:
                increase = False
            masterList[count].append(i)
            
            if increase:
                count += 1
            else:
                count -= 1
        result = ""
        for n in range(numRows):
            for i in masterList[n]:
                result += i
            # result+=str(masterList[n])
            
        # print(result)
        # print(masterList)
        return result
