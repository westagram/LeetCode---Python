class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        masterDict = collections.defaultdict(list)
        for word in strs:
            masterDict[tuple(sorted(word))].append(word)
        return masterDict.values()