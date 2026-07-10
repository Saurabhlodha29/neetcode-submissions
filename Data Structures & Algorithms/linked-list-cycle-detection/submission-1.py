# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast = ListNode()
        slow = ListNode()

        fast.next = slow.next = head

        while fast != slow:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
            if fast == None or fast.next == None:
                return False