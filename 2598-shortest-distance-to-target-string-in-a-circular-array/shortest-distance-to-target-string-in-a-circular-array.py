class Solution:
    def closestTarget(self, words: List[str], target: str, st: int) -> int:
        f={}
        for idx,i in enumerate(words):
            if i in f:
                f[i].append(idx)
            else:
                f[i]=[idx]
        if target in f:
            ans=float('inf')
            n=len(words)
            for i in f[target]:
                if i==st:
                    return 0
                elif i<st:
                    ans=min(ans,st-i,n-st+i)
                else:
                    ans=min(ans,i-st,n+st-i)
            return ans
        else:
            return -1
        