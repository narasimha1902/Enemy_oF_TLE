class Solution:
    def closestTarget(self, words: List[str], target: str, st: int) -> int:
        n=len(words)
        ans=float('inf')
        for idx,i in enumerate(words):
            if target==i:
                if idx==st:
                    return 0
                ans=min(ans,abs(idx-st),n-abs(st-idx))
        return ans if ans!=float('inf') else -1
        