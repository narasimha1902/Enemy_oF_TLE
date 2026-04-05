from collections import Counter
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        ans=0
        f=Counter(s)
        for i in "abcdefghijklm":
            m=chr(ord('a')+ord('z')-ord(i))
            ans+=abs(f.get(i,0)-f.get(m,0))
        for i in "01234":
            m=chr(ord('0')+ord('9')-ord(i))
            ans+=abs(f.get(i,0)-f.get(m,0))
        return ans
                
            