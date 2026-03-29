class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n=len(s)
        i=0
        while i<(n+1)//2:
            if s[i]==s[n-i-1]:
                return i
            i+=1
        return -1