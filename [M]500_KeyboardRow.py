class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        masterSet = {"QWERTYUIOP", "ASDFGHJKL", "ZXCVBNNMM"}
        retList = []
        for word in words:
            upperWord = word.upper()
            for row in masterSet:
                if len(set(upperWord)) == len(set(upperWord).intersection(row)):
                    retList.append(word)
        return retList