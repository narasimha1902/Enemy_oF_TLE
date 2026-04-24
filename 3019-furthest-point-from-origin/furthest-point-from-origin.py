class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        for i in moves:
            if i=='L':
                l+=1
            elif i=='R':
                r+=1
        u=len(moves)-l-r
        return abs(l-r)+u
         