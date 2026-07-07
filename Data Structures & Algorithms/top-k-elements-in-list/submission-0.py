class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        distribution = dict()
        ans = list()

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for element,frequency in freq.items():
            if frequency not in distribution:
                distribution[frequency] = [element]
            else:
                distribution[frequency].append(element)

        while k:
            if len(distribution) != 0:
                maxFreq = max(distribution.keys())
                maxEl = distribution[maxFreq].pop()
                ans.append(maxEl)
                if len(distribution[maxFreq]) == 0:
                    distribution.pop(maxFreq)
                k -= 1

        return ans

                

        

        