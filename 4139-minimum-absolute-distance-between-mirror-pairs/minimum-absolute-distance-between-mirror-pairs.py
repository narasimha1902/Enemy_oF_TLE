class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def mp(val):
            res=0
            while val>0:
                rem=val%10
                val//=10
                res=res*10+rem
            return res
        f={}
        n=len(nums)
        ans=float('inf')
        for i in range(n):
            if nums[i] in f:
                ans=min(ans,abs(f[nums[i]]-i))
            f[mp(nums[i])]=i
        return -1 if ans==float('inf') else ans
