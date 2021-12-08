class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        masterGraph = dict()
        for idx, value in enumerate(rooms):
            masterGraph[idx] = value
        visited = {0}
        self.dfs(0, masterGraph, visited)
        return len(visited) == len(rooms)
        
    def dfs(self, node, masterGraph, visited):
        for nextNode in masterGraph[node]:
            if nextNode in visited:
                continue
            visited.add(nextNode)
            self.dfs(nextNode, masterGraph, visited)
