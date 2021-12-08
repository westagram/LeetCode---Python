# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        retList = []
        reverse = False
        while len(queue) != 0:
            tempList = []
            for i in range(len(queue)):
                curNode = queue.pop(0)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                tempList.append(curNode.val)
            if reverse:
                retList.append(tempList[::-1])
            else:
                retList.append(tempList)
            reverse = not reverse
        return retList
