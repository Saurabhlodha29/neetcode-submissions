from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append a 0 dummy bar to flush out all remaining bars in the stack at the end
        heights.append(0)
        stack = [] # Stores tuples of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # If the current bar is shorter than the bar at the top of the stack,
            # it means the taller bar cannot extend any further to the right.
            while stack and stack[-1][1] > h:
                pop_i, pop_h = stack.pop()
                # Calculate the width from the original start index of the popped bar
                width = i - pop_i
                max_area = max(max_area, pop_h * width)
                # The current shorter bar can retroactively extend back to the popped bar's starting position
                start = pop_i
                
            stack.append((start, h))
            
        # Restore the original array state (good practice)
        heights.pop()
        return max_area
