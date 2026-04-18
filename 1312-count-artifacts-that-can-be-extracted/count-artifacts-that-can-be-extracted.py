class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug=set(r*n+c for r,c in dig)
        return sum(all(i*n+j in dug for i in range(a,c+1) for j in range(b,d+1)) for a,b,c,d in artifacts)
            
