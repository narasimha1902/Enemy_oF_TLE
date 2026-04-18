class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        f={}
        ans=0
        dug=set(r*n+c for r,c in dig)
        for t in artifacts:
            a,b,c,d=t
            claim=True
            for i in range(a,c+1):
                for j in range(b,d+1):
                    if i*n+j not in dug:
                        claim=False
                        break
            if claim:
                ans+=1
        return ans
            
