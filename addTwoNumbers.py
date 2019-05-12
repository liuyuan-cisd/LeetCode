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
        c=0
        num1=0
        num2=0
        while p1:
            num1+=p1.val*(10**c)
            c+=1 
            p1=p1.next
        c=0
        while p2:
            num2+=p2.val*(10**c)
            p2=p2.next
            c+=1
        sum=num1+num2
        head=ListNode(sum%10)
        p=head
        sum=sum//10
        print(sum)
        flag=True
        while flag:
            temp=sum%(10)
            if sum==0:
                flag=False
            else:
                s=ListNode(temp)
                p.next=s
                p=p.next
                sum=sum//10
            c+=1
            
        return head
            
