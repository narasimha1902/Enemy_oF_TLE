class Solution:
    def numberOfWeeks(self, ms: List[int]) -> int:
        ts=sum(ms)
        mx=max(ms)
        rem=ts-mx
        if mx<=rem+1:
            return ts
        else:
            return 2*rem+1