# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        orderedList = []
        self.DFS(root, orderedList)
        for i in range(1, len(orderedList)):
            if orderedList[i] <= orderedList[i-1]:
                return False
        return True
        
    
    def DFS(self, root, DFSList):
        if root.left != None:
            self.DFS(root.left, DFSList)
        DFSList.append(root.val)
        if root.right != None:
            self.DFS(root.right, DFSList)
        
        
