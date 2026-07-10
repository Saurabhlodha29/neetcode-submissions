class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            l1 = -heapq.heappop(stones)
            l2 = -heapq.heappop(stones)

            if l1 != l2:
                remainder = -abs(l1-l2)
                heapq.heappush(stones,remainder)
            

        if len(stones) == 0:
            return 0
        
        return -stones[0]

            