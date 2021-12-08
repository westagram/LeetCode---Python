# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        returnList = []
        while queue != []:
            returnList.append(queue[-1].val)
            print(returnList)
            queueLen = len(queue)
            for idx in range(len(queue)):
                if queue[idx].left:
                    queue.append(queue[idx].left)
                if queue[idx].right:
                    queue.append(queue[idx].right)
            queue = queue[queueLen:]
        return returnList
                
