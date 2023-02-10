class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # Create a set and append it as we go
        # Run a dfs algorithm to go through the tree
        output = set()
        length = len(s)
        self.dfs("", output, s, length)
        return list(output)

    def dfs(self, cur_string, output, s, length):
        if len(cur_string) == length:
            output.add(cur_string)
            return
        for idx,char in enumerate(s):
            if char.isalpha():
                for i in [char.upper(), char.lower()]:
                    self.dfs(cur_string+i, output, s[idx+1:], length)
            else:
                self.dfs(cur_string+char, output, s[idx+1:], length)