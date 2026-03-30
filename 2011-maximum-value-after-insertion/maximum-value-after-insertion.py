class Solution:
    def maxValue(self, n: str, x: int) -> str:
        def getp(st):
            le=len(st)
            if st[0]=='-':
                pos=1
                while pos<le and x>=int(st[pos]):
                    pos+=1
            else:
                pos=0
                while pos<le and x<=int(st[pos]):
                    pos+=1
            return pos
        pos=getp(n)
        return n[:pos]+str(x)+n[pos:]
        
            