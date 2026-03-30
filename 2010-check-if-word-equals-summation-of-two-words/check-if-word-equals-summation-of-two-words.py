class Solution:
    def isSumEqual(self, fw: str, sw: str, tar: str) -> bool:
        def conv(st):
            res=""
            n=len(st)
            for i in range(n):
                res=res+str(ord(st[i])-97)
            return int(res)
        return conv(fw)+conv(sw)==conv(tar)
                