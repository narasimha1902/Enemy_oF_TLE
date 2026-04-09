import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap=[]
        seen=set()
        for i in nums:
            if i not in seen:
                heapq.heappush(heap,i)
                if len(heap)>3:
                    heapq.heappop(heap)
                seen.add(i)
        return heapq.heappop(heap) if len(heap)==3 else max(heap)
        