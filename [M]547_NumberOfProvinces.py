class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        masterDict = {i:[] for i in range(len(isConnected))}
        for row in range(len(isConnected)):
            for col in range(len(isConnected[row])):
                if isConnected[row][col] and row != col:
                    masterDict[row].append(col)
        visited = set()
        nProvinces = 0
        for k in masterDict:
            if k not in visited:
                nProvinces += 1
                self.dfs(k, masterDict, visited)
        return nProvinces
    
    def dfs(self, key, masterDict, visited):
        if key in visited: return
        visited.add(key)
        for v in masterDict[key]:
            self.dfs(v, masterDict, visited)
