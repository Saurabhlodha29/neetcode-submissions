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
                while num + 1 in numset:
                    num += 1
                    length += 1

                longest = max(longest, length)
                length = 1


        return longest