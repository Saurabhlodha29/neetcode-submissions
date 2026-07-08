class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        l = [0] * len(nums)
        ans = list()

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for elem, occ in freq.items():
            if l[occ-1] != 0:
                l[occ-1].append(elem)
            else:
                l[occ-1] = [elem]

        for i in range(len(nums)-1,-1,-1):
            if k:
                if l[i] == 0:
                    continue
                else:
                    while k:
                        ans.append(l[i].pop(0))
                        k -= 1
                        if len(l[i]) == 0:
                            break
            else:
                break

        return ans


                

        

        