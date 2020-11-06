class Solution:
    def firstUniqChar(self, s: str) -> int:
        discardSet = set()
        uniqueDict = dict()
        for i in range(len(s)):
            if s[i] not in uniqueDict and s[i] not in discardSet:
                uniqueDict[s[i]] = i
            elif s[i] in uniqueDict and s[i] not in discardSet:
                del uniqueDict[s[i]]
                discardSet.add(s[i])
        sortedUniqueTuple = sorted(uniqueDict.items(), key=lambda item: item[1])
        if len(uniqueDict) == 0:
            return -1
        return sortedUniqueTuple[0][1]
