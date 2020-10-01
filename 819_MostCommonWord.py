import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        par = re.sub("[^a-zA-Z]", " ",paragraph)
        splitStr = par.split()
        masterDict = dict()
        for i in range(len(splitStr)):
            splitStr[i] = splitStr[i].lower()
            if splitStr[i] in masterDict:
                masterDict[splitStr[i]] += 1
            else:
                masterDict[splitStr[i]] = 1
        sortedDict = sorted(masterDict.items(), key = lambda kv: kv[1], reverse = True)
        for w in sortedDict:
            if w[0] not in banned:
                return w[0]
