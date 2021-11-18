# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        self.binaryTreeHelper(root, "", ret)
        return ret
        
    def binaryTreeHelper(self, root, path, allPaths):
        path += str(root.val) if path == "" else "->" + str(root.val)
        if root.left is None and root.right is None:
            allPaths.append(path)
            return
        if root.left is not None:
            self.binaryTreeHelper(root.left, path, allPaths)
        if root.right is not None:
            self.binaryTreeHelper(root.right, path, allPaths)
