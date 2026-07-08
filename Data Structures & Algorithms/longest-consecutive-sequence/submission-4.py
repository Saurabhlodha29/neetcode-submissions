class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        numset = set(nums)
        numlist = list(numset)

        largestsize = 1

        while numlist:

            st = min(numlist)
            currsize = 1

            while st + 1 in numset:
                numlist.remove(st)
                st += 1
                currsize += 1

            numlist.remove(st)
            largestsize = max(largestsize, currsize)

        return largestsize