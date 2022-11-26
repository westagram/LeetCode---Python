class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currentPrefix = strs[0]
        for idx, word in enumerate(strs[1:]):
            newStr = ""
            for n in range(min(len(currentPrefix), len(word))):
                if currentPrefix[n] != word[n]:
                    break
                newStr += currentPrefix[n]
            currentPrefix = newStr
        return currentPrefix