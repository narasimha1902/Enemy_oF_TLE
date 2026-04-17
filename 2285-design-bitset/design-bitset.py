class Bitset:

    def __init__(self, size: int):
        self.f=set()
        self.n=size
        self.z=set(range(self.n))
    def fix(self, idx: int) -> None:
        if idx not in self.f:
            self.f.add(idx)
            self.z.remove(idx)
    def unfix(self, idx: int) -> None:
        if idx in self.f:
            self.f.remove(idx)
            self.z.add(idx)
    def flip(self) -> None:
        self.f,self.z=self.z,self.f
    def all(self) -> bool:
        return len(self.f)==self.n 
    def one(self) -> bool:
        return len(self.f)>=1
    def count(self) -> int:
        return len(self.f)
    def toString(self) -> str:
        res=['0']*self.n
        for i in self.f:
            res[i]='1'
        return ''.join(res)


        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()