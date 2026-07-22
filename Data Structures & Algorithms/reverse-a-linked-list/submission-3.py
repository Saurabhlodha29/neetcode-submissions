# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        temp1 = head
        temp2 = temp1.next
        temp0 = None

        while temp1.next is not None:
            temp1.next = temp0
            temp0 = temp1
            if temp2:
                temp1 = temp2
                temp2 = temp2.next
        temp1.next = temp0
        return temp1

