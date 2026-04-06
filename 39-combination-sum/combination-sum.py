class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        res=[]
        def bc(st,path,target,s):
            if s==target:
                res.append(path[:])
                return
            if s>target:
                return
            for i in range(st,len(cand)):
                path.append(cand[i])
                bc(i,path,target,s+cand[i])
                path.pop()
        bc(0,[],target,0)
        return res 