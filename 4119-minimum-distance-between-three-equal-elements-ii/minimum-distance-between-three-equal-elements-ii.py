class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        f={}
        n=len(nums)
        ans=float('inf')
        for i in range(n):
            if nums[i] in f:
                f[nums[i]].append(i)
                if len(f[nums[i]])>=3:
                    a,b,c=f[nums[i]][-3],f[nums[i]][-2],f[nums[i]][-1]
                    ans=min(ans,abs(a-b)+abs(b-c)+abs(c-a))
            else:
                f[nums[i]]=[i]
        return -1 if ans==float('inf') else ans
