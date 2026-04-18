class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            idx=abs(nums[i])-1
            if nums[idx]>0:
                nums[idx]=-nums[idx]
        res=[]
        for i in range(n):
            if nums[i]>0:
                res.append(i+1)
        return res