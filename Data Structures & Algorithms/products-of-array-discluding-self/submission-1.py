class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        stored = [0]*len(nums)
        prod = 1
        for i in range(1,len(nums)):
            prod *= nums[i]
        stored[0] = prod

        for i in range(1,len(nums)):
            if nums[i] != 0:
                if stored[i-1] == 0 and nums[i] != 0:
                    stored[i] = 0
                else:
                    stored[i] = (stored[i-1]*nums[i-1])//nums[i]
            else:
                flag = 1
                for j in range(len(nums)):
                    if j == i:
                        continue
                    else:
                        flag *= nums[j]

                stored[i] = flag
        
        return stored
