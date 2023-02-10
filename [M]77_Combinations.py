class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        self.dfs(output, [], 1, n, k)
        return output
    
    def dfs(self, output, cur_list, cur_int, n, k):
        if len(cur_list) == k:
            output.append(cur_list)
            return
        for i in range(cur_int, n+1):
            self.dfs(output, cur_list+[i], i+1, n, k)

