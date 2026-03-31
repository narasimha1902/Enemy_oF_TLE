class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        if t>8:
            return []
        res=[]
        for i in range(12):
            for j in range(60):
                if bin(i).count('1')+bin(j).count('1')==t:
                    res.append(f"{i}:{j:02}")
        return res