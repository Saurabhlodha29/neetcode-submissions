from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search runtime
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            partition_x = (low + high) // 2
            partition_y = half_len - partition_x
            
            # Boundary conditions for nums1
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            
            # Boundary conditions for nums2
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            
            # Check if we found the correct partition point
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Odd total number of elements
                if (m + n) % 2 != 0:
                    return float(max(max_left_x, max_left_y))
                # Even total number of elements
                else:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
            
            # Too far right in nums1, move partition left
            elif max_left_x > min_right_y:
                high = partition_x - 1
                
            # Too far left in nums1, move partition right (Fixes the infinite loop)
            else:
                low = partition_x + 1
                
        raise ValueError("Input arrays are not sorted or contain invalid elements.")
