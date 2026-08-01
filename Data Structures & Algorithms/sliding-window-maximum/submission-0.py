from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Store the final maximum values for each window position
        result = []
        
        # Store indices of elements in a monotonic decreasing order
        queue = deque()
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window bound
            if queue and queue[0] < i - k + 1:
                queue.popleft()
                
            # 2. Maintain monotonic decreasing property
            # Remove indices of all elements smaller than the current element
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop(0) if isinstance(queue, list) else queue.pop()
                
            # 3. Append the current element's index
            queue.append(i)
            
            # 4. Append the max element to the result once the first window is full
            if i >= k - 1:
                result.append(nums[queue[0]])
                
        return result
