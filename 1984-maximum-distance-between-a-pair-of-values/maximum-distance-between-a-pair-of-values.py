class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1=0
        p2=0
        n=len(nums1)
        n2=len(nums2)
        ans=0
        while p1<n and p2<n2:
            if nums1[p1]>nums2[p2]:
                p1+=1
                p2=max(p1,p2)
            else:
                ans=max(ans,p2-p1)
                p2+=1
        return ans

