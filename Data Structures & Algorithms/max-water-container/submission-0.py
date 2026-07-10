class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l = 0
        r = len(heights)-1

        while l < r:
            effective_height = min(heights[l],heights[r])
            effective_area = (r-l)*effective_height

            max_area = max(effective_area,max_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area
