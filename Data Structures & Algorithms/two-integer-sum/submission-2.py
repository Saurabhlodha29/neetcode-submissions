class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = dict()

        for i,num in enumerate(nums):
            diff = target-num 
            if diff in lookup:
                return [lookup[diff],i]
            
            lookup[num] = i