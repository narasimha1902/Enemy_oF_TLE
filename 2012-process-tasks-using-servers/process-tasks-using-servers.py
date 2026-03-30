import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        h=[]
        for i,w in enumerate(servers):
            heapq.heappush(h,(w,i))
        busy=[]
        n=len(tasks)
        res=[None]*n
        currt=0
        for i in range(n):
            currt=max(currt,i)
            while busy and busy[0][0]<=currt:
                _,w,idx=heapq.heappop(busy)
                heapq.heappush(h,(w,idx))
            if not h:
                currt=busy[0][0]
                while busy and busy[0][0] <= currt:
                    _, w, idx = heapq.heappop(busy)
                    heapq.heappush(h, (w, idx))
            w,idx=heapq.heappop(h)
            res[i]=idx
            heapq.heappush(busy,(currt+tasks[i],w,idx))
        return res

