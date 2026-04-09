class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        ll=nums[:3]
        return sum(ll)-min(ll)-max(ll)        