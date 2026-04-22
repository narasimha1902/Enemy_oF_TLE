from collections import Counter
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        f=Counter(dictionary)
        if len(queries[0])<3:
            return queries
        def cng(st,fr):
            le=len(st)
            ret=5
            for i in fr:
                ret=min(ret,sum(1 for p in range(le) if st[p]!=i[p]))
            return ret
        res=[]
        for i in queries:
            if i in f:
                res.append(i)
            elif cng(i,f)<=2:
                res.append(i)
        return res 
