class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        masterDict = {}
        for pat, word in zip(pattern, s.split()):
            if pat not in masterDict:
                masterDict[pat] = word
            else:
                if masterDict[pat] != word:
                    return False
        return len(set(masterDict.keys())) == len(set(masterDict.values()))