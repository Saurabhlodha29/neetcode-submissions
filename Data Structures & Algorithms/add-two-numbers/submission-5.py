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

        while temp1 or temp2 or carry:
            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0
            currsum = val1 + val2 + carry

            temp.next = ListNode(currsum%10)
            carry = currsum//10
            temp = temp.next
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        return new.next
