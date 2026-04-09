class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        a=nums[0]
        b=nums[1]
        c=nums[2]
        if a<b<c or c<b<a:
            return b
        elif a<c<b or b<c<a:
            return c
        else:
            return a

        
