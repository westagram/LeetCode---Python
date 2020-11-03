# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        returnList = []
        self.inorderUtil(root, returnList)
        return returnList
    
    def inorderUtil(self, root, l):
        if root.left != None:
            self.inorderUtil(root.left, l)
        l.append(root.val)
        if root.right != None:
            self.inorderUtil(root.right, l)
        
