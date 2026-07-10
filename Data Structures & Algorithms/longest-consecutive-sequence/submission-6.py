class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        numset = set(nums)

        longest = 0
        length = 1


        for num in numset:
            if num-1 in numset:
                continue
            else:
                while True:
                    if num+1 in numset:
                        num += 1
                        length += 1
                    else:
                        longest = max(longest,length)
                        length = 1
                        break


        return longest