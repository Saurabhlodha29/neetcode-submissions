class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left , right = 0, len(nums)-1
        minidx = -1

        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
            
        minidx = left
        
        if nums[minidx] <= target and nums[-1] >= target:
            left, right = minidx, len(nums)-1
        else:
            left, right = 0, minidx-1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
                
        return -1