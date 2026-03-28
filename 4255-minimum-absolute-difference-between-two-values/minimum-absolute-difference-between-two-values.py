class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        l1=l2=-1
        ans=float('inf')
        n=len(nums)
        for i in range(n):
            if nums[i]==2:
                l2=i
                if l1!=-1:
                    ans=min(ans,i-l1)
            if nums[i]==1:
                l1=i
                if l2!=-1:
                    ans=min(ans,i-l2)
        return ans if ans!=float('inf') else -1