class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod=10**9+7
        for i in range(len(nums)):
            nums[i]%=mod
        for q in queries:
            l,r,i,m=q
            m%=mod
            idx=l
            while idx<=r:
                nums[idx]=(nums[idx]*m)%mod
                idx+=i
        xor=0
        for i in range(len(nums)):
            xor^=nums[i]
        return xor
