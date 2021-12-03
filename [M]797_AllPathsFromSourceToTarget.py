class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        masterGraph = dict()
        for idx, dest in enumerate(graph):
            masterGraph[idx] = dest
        retList = []
        self.dfs(masterGraph, 0, [0], retList)
        return retList
        
    def dfs(self, masterGraph, curNode, path, retList):
        if curNode == len(masterGraph) - 1:
            retList.append(path)
            return
        for i in masterGraph[curNode]:
            self.dfs(masterGraph, i, path+[i], retList)
