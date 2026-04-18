class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        f={}
        for t in artifacts:
            a,b,c,d=t
            idx=[]
            for i in range(a,c+1):
                for j in range(b,d+1):
                    pos=i*n+j
                    idx.append(pos)
            for pos in idx:
                f[pos]=idx
        ans=0
        digged={}
        for r,c in dig:
            pos=r*n+c
            digged[pos]=True
            if pos in f:
                if all(i in digged for i in f[pos]):
                    ans+=1
        return ans
            
