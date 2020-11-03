# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sumDict = dict()
        self.deepestLeavesSumUtil(root, sumDict, 0)
        return(sumDict[max(sumDict)])
            
    def deepestLeavesSumUtil(self, root, sumDict, level):
        if level not in sumDict:
            sumDict[level] = root.val
        else:
            sumDict[level] += root.val
        if root.left != None:
            self.deepestLeavesSumUtil(root.left, sumDict, level+1)
        if root.right != None:
            self.deepestLeavesSumUtil(root.right, sumDict, level+1)
        
