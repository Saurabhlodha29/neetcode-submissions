# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:   #Finding middle of the LL
            slow = slow.next
            fast = fast.next.next
        
        start2 = slow.next
        prev = None
        slow.next = None
        start1 = head

        while start2:              #Reversing the 2nd Half
            curr = start2.next
            start2.next = prev
            prev = start2
            start2 = curr
            
        start2 = prev

        while start1 and start2:   #Merging both alternatively
            curr1 = start1.next
            curr2 = start2.next
            start1.next = start2
            start1 = curr1
            start2.next = start1
            start2 = curr2
        
            


