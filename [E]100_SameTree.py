# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pTree = []
        qTree = []
        self.getTreeValue(pTree, p)
        self.getTreeValue(qTree, q)
        print(pTree, qTree)
        return pTree == qTree
    
    def getTreeValue(self, l, tree):
        if tree is None:
            l.append(None)
            return
        l.append(tree.val)
        self.getTreeValue(l, tree.left)
        self.getTreeValue(l, tree.right)