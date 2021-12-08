# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        masterList = []
        self.dfs(root, "", masterList)
        return sum(masterList)
        
    def dfs(self, root, curIntStr, masterList):
        curIntStr += str(root.val)
        if root.left is None and root.right is None:
            masterList.append(int(curIntStr))
        if root.left:
            self.dfs(root.left, curIntStr, masterList)
        if root.right:
            self.dfs(root.right, curIntStr, masterList)
