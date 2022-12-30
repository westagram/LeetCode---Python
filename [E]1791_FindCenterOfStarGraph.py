class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgesDict = collections.defaultdict(list)
        for pair in edges:
            edgesDict[pair[0]].append(pair[1])
            edgesDict[pair[1]].append(pair[0])
        return sorted(edgesDict.items(), key = lambda x: len(x[1]), reverse = True)[0][0]