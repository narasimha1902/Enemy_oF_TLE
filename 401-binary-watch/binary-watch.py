class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        return [f"{h}:{m:02d}" for m in range(60) for h in range(12) if bin(h).count('1')+bin(m).count('1')==t]