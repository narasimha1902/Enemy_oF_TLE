class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        f={}
        ans=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==2:
                if 1 in f:
                    ans=abs(i-f[1]) if ans==-1 else min(ans,abs(i-f[1])) 
                f[2]=i
            if nums[i]==1:
                if 2 in f:
                    ans=abs(i-f[2]) if ans==-1 else min(ans,abs(i-f[2]))
                f[1]=i
        return ans