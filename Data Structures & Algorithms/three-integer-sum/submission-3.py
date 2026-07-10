class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = list()
        
        nums.sort()

        for i in range(1,len(nums)):
            l = i-1
            r = i+1

            while l < r and l > -1 and r < len(nums):
                if nums[i] + nums[r] + nums[l] == 0:
                    triplet = [nums[l],nums[i],nums[r]]
                    if triplet not in ans:
                        ans.append(triplet)
                    l -= 1
                    r += 1
                elif nums[i] + nums[r] + nums[l] < 0:
                    r += 1
                elif nums[i] + nums[r] + nums[l] > 0:
                    l -= 1
            
            

        return ans
