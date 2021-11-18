# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        output = True
        if root.left:
            output = root.val == root.left.val
            output = output and self.isUnivalTree(root.left)
        if root.right:
            output = root.val == root.right.val
            output = output and self.isUnivalTree(root.right)
        print(root.val, output)
        return output
