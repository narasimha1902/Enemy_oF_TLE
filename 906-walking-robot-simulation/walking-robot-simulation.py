class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs=set(map(tuple,obstacles))
        x,y=0,0
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        dir=0
        ans=0
        for i in commands:
            if i==-1:
                dir=(dir+1)%4
            elif i==-2:
                dir=(dir-1)%4
            else:
                dx,dy=dirs[dir]
                for _ in range(i):
                    if (x+dx,y+dy) in obs:
                        break
                    x+=dx
                    y+=dy
                ans=max(ans,x*x+y*y)
        return ans