class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.getHashString(s) == self.getHashString(t)

    def getHashString(self, inputString):
        masterDict = dict()
        for char in inputString:
            if char in masterDict:
                masterDict[char] += 1
            else:
                masterDict[char] = 1
        return masterDict
