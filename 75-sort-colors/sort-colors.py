class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=nums.copy()
        p1=0
        p2=len(nums)-1
        for i in arr:
            if i==0:
                nums[p1]=0
                p1+=1
            elif i==2:
                nums[p2]=2
                p2-=1
            print(nums)
            print(p1,p2)
        while p1<=p2:
            nums[p1]=1
            p1+=1

