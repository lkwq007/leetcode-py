class Bitset:

    def __init__(self, size: int):
        self.cnt=0
        self.size=size
        self.is_flip=False
        self.lst=[0]*size

    def fix(self, idx: int) -> None:
        val=1 if self.is_flip else 0
        if self.lst[idx]==val:
            self.cnt+=1
        self.lst[idx]=1-val

    def unfix(self, idx: int) -> None:
        val=1 if self.is_flip else 0
        if self.lst[idx]==1-val:
            self.cnt-=1
        self.lst[idx]=val

    def flip(self) -> None:
        self.cnt=self.size-self.cnt
        self.is_flip=not self.is_flip            

    def all(self) -> bool:
        return self.cnt==self.size

    def one(self) -> bool:
        return self.cnt>0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        val=1 if self.is_flip else 0
        return "".join([("1" if val+item==1 else "0") for item in self.lst])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

class Bitset:

    def __init__(self, size: int):
        self.cnt=0
        self.size=size
        self.is_flip=False
        self.lst=[0]*size

    def fix(self, idx: int) -> None:
        if self.is_flip:
            if self.lst[idx]==1:
                self.cnt+=1
            self.lst[idx]=0
        else:
            if self.lst[idx]==0:
                self.cnt+=1
            self.lst[idx]=1

    def unfix(self, idx: int) -> None:
        if self.is_flip:
            if self.lst[idx]==0:
                self.cnt-=1
            self.lst[idx]=1
        else:
            if self.lst[idx]==1:
                self.cnt-=1
            self.lst[idx]=0

    def flip(self) -> None:
        self.cnt=self.size-self.cnt
        self.is_flip=not self.is_flip            

    def all(self) -> bool:
        return self.cnt==self.size

    def one(self) -> bool:
        return self.cnt>0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        val=1 if self.is_flip else 0
        return "".join([("1" if val+item==1 else "0") for item in self.lst])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()