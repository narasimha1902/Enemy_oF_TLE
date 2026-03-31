class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        if t>8:
            return []
        res=[]
        mp=[8,4,2,1,32,16,8,4,2,1]
        def bc(i,h,m,c):
            if c==t and h<=11 and m<=59:
                res.append(f"{h}:{m:02d}")
                return
            if c>t or h>11 or m>59 or i>9:
                return
            if i<4:
                bc(i+1,h+mp[i],m,c+1)
            else:
                bc(i+1,h,m+mp[i],c+1)
            bc(i+1,h,m,c)
        bc(0,0,0,0)
        return res