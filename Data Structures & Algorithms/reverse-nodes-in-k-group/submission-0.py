# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node to track the new head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # group_prev always tracks the node right before the current k-group
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left to reverse
            kth_node = self.getKthNode(group_prev, k)
            if not kth_node:
                break
                
            # Track the start of the next group
            group_next = kth_node.next
            
            # Reverse the current k-group
            prev = kth_node.next  # Connect tail of reversed group to next group
            curr = group_prev.next
            
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # Connect the previous part of the list to the new head of reversed group
            temp = group_prev.next
            group_prev.next = kth_node
            
            # Move group_prev to the end of the reversed group
            group_prev = temp
            
        return dummy.next

    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
