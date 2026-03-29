import heapq
class EventManager:
    def __init__(self, events: list[list[int]]):
        self.n=len(events)
        self.f={}
        self.h=[]
        for e,p in events:
            self.f[e]=p
            heapq.heappush(self.h,(-p,e))
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.f[eventId]=newPriority
        heapq.heappush(self.h, (-newPriority, eventId))
    def pollHighest(self) -> int:
        while self.h:
            p,evd=heapq.heappop(self.h)
            if evd in self.f and self.f[evd]==-p:
                del self.f[evd]
                return evd
        return -1
# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()