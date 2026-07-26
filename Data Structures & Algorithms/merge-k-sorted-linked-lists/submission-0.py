import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a dummy node to easily build the result list
        dummy = ListNode(0)
        current = dummy
        
        # Initialize the min-heap
        heap = []
        
        # Push the head of each non-empty linked list into the heap
        # We include a counter variable `i` to prevent comparison errors between ListNodes
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
                
        # Extract the minimum node and add its next node to the heap
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # If the extracted node has a next element, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
