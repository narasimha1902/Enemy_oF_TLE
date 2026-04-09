class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        a=nums[0]
        b=nums[1]
        c=nums[2]
        return a+b+c-min(a,b,c)-max(a,b,c)
        
