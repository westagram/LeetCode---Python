# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Num = int(self.getReversedNum(l1))
        l2Num = int(self.getReversedNum(l2))
        sumL1L2 = str(l1Num + l2Num)
        print(sumL1L2)
        
        headListNode = ListNode(val=int(sumL1L2[-1]))
        print(headListNode)
        tempListNode = headListNode
        for i in range(len(sumL1L2)):
            if i == len(sumL1L2) - 1:
                break
            while tempListNode.next != None:
                tempListNode = tempListNode.next
            tempListNode.next = ListNode(sumL1L2[-2-i])
        return headListNode
            
            
            
    
    def getReversedNum(self, listNode):
        string = ""
        if listNode.next != None:
            string = self.getReversedNum(listNode.next)
        return string + str(listNode.val)
        
          
