# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sumN: int) -> bool:
        if root == None:
            return False
        retBool = False
        newSum = sumN - root.val
        if newSum == 0 and root.left == None and root.right == None:
            return True
        if root.left != None:
            retBool = self.hasPathSum(root.left, newSum)
        if retBool:
            return retBool
        if root.right != None:
            retBool = self.hasPathSum(root.right,newSum)
        return retBool
