class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Create a dict to keep track of word abb = {a:0, b:1} => 011
        # Loop and if word matches pattern, append to return list
        ret = []
        patList = self.getPattern(pattern)
        for word in words:
            if self.getPattern(word) == patList:
                ret.append(word)
        return ret

    def getPattern(self, word):
        masterDict = {}
        retList = []
        idx = 0
        for char in word:
            if char not in masterDict:
                masterDict[char] = idx
                idx += 1
            retList.append(masterDict[char])
        return retList