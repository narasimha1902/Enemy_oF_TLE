class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        bot=0
        top=sum(grid[0])
        ans=float('inf')
        for i in range(n):
            top-=grid[0][i]
            ans=min(ans,max(top,bot))
            bot+=grid[1][i]
        return ans