# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        return self.preorder_traversal(root)
        
        
    def preorder_traversal(self, root):
        if root is None:
            return
        queue = [root]
        is_odd = True
        
        while len(queue) > 0:
            prev_node = None
            for node_idx in range(len(queue)):
                cur_node = queue.pop(0)
                if is_odd:
                    if cur_node.val % 2 == 0:
                        return False
                else:
                    if cur_node.val % 2 != 0:
                        return False
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if prev_node and is_odd and cur_node.val <= prev_node:
                    return False
                if prev_node and not is_odd and cur_node.val >= prev_node:
                    return False
                prev_node = cur_node.val
            is_odd = False if is_odd else True
            cur_queue_val = [i.val for i in queue]
        return True
