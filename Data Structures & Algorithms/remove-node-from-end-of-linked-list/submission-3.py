# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return
        dummy = ListNode
        dummy.next = head
        slow = dummy
        fast = dummy.next

        while n and fast:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

