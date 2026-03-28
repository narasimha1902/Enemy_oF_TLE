class Solution:
    def concatHex36(self, n: int) -> str:
        def solve(val,base):
            chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res=[]
            while val>0:
                res.append(chars[val%base])
                val//=base
            return "".join(res[::-1])
        sq=n*n
        return solve(sq,16)+solve(sq*n,36)
            