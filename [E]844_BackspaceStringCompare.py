class Solution:
    def getFinalString(self, s):
        return_string = ""
        for subStr in s:
            if subStr == "#":
                return_string = return_string[:-1]
            else:
                return_string += subStr
        return return_string
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.getFinalString(s) == self.getFinalString(t)
        
