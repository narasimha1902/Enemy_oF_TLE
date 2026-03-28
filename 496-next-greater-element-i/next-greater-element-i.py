class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f={}
        n=len(nums1)
        for i in range(n):
            f[nums1[i]]=i
        res=[-1]*n
        n=len(nums2)
        stack=[]
        for i in range(n):
            while stack and nums2[i]>nums2[stack[-1]]:
                idx=stack.pop()
                if nums2[idx] in f:
                    res[f[nums2[idx]]]=nums2[i]
            stack.append(i)
        return res
