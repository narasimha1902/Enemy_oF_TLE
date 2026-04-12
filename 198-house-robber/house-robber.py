class Solution:
    def rob(self, nums: List[int]) -> int:
        pre2=pre1=0
        for i in nums:
            curr=max(pre2+i,pre1)
            pre2=pre1
            pre1=curr
        return pre1
