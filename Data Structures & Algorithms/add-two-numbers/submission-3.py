# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        carry = 0

        temp = new
        temp1 = l1
        temp2 = l2

        while temp1 and temp2:
            currsum = temp1.val + temp2.val + carry
            temp.val = (currsum)%10
            carry = currsum//10
            temp1 = temp1.next
            temp2 = temp2.next
            if temp1 or temp2:
                temp.next = ListNode()
                temp = temp.next
            

        while temp1:
            temp.val = (temp1.val + carry)%10
            carry = (temp1.val + carry)//10
            temp1 = temp1.next
            if temp1:
                temp.next = ListNode()
                temp = temp.next
            

        while temp2:
            temp.val = (temp2.val + carry)%10
            carry = (temp2.val + carry)//10
            temp2 = temp2.next
            if temp2:
                temp.next = ListNode()
                temp = temp.next

        if carry:
            temp.next = ListNode(carry)

        return new
