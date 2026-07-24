"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        #Step-1 : Creating the copy nodes in the same LL in alternate fashion
        curr = head
        while curr:
            copy = Node(curr.val,curr.next)
            curr.next = copy
            curr = curr.next.next

        #Step-2 : Assigning random to each copy node
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = curr.next.next
            
        #Step-3 : Separating both LLs
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return copy_head
        

        