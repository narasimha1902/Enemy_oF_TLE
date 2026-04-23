class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n=len(nums)
        f={}
        res=[0]*n
        for i in range(n):
            if nums[i] in f:
                pre,sm,cnt=f[nums[i]]
                res[i]=cnt*(abs(pre-i))+sm
                f[nums[i]]=[i,res[i],cnt+1]
            else:
                f[nums[i]]=[i,0,1]
        f={}
        for i in range(n-1,-1,-1):
            if nums[i] in f:
                pre,sm,cnt=f[nums[i]]
                cv=cnt*(abs(pre-i))+sm
                res[i]+=cv
                f[nums[i]]=[i,cv,cnt+1]
            else:
                f[nums[i]]=[i,0,1]
        return res
