class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1=0
        n=len(s)
        for i in t:
            if p1<n and s[p1]==i:
                p1+=1
        return True if p1==n else False