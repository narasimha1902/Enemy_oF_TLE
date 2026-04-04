import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for i in arr:
            heapq.heappush(heap,(abs(i-x),i))
        res=[]
        while k>0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return sorted(res)
