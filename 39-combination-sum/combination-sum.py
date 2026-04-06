class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        res=set()
        def bc(path,target):
            if sum(path)==target:
                res.add(tuple(sorted(path[:])))
                return
            if sum(path)>target:
                return
            for i in cand:
                path.append(i)
                bc(path,target)
                path.pop()
        bc([],target)
        return list(res) 