# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        valList = []
        iterNode = head
        while iterNode != None:
            valList.append(iterNode.val)
            iterNode = iterNode.next
        return valList == self.reverse(valList)
    
    def reverse(self, s):
        return s[::-1]
