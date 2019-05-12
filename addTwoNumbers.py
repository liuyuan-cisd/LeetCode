# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1=l1
        p2=l2
        carry=0
        head=ListNode(0)
        p=head
        while p1 or p2 or carry!=0:
            p1_value=0
            p2_value=0
            if p1:
                p1_value=p1.val
                p1=p1.next
            if p2:
                p2_value=p2.val
                p2=p2.next
            sum=p1_value+p2_value+carry
            carry=sum//10
            sum=sum%10
            p.next=ListNode(sum)
            p=p.next
        return head.next
