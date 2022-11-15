# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, total):
        if root is None:
            return total
        else:
            total += 1
            return max(self.dfs(root.left, total), self.dfs(root.right, total))