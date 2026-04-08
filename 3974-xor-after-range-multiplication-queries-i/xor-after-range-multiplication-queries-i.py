class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod=10**9+7
        for q in queries:
            l,r,k,m=q
            for idx in range(l,r+1,k):
                nums[idx]=(nums[idx]*m)%mod
        xor=0
        for i in range(len(nums)):
            xor^=nums[i]
        return xor
