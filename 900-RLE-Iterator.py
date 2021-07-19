class RLEIterator:

    def __init__(self, A: List[int]):
        self.pos=0
        self.lst=A

    def next(self, n: int) -> int:
        ret=0
        while n>0:
            if self.pos<len(self.lst):
                if self.lst[self.pos]<n:
                    n-=self.lst[self.pos]
                    self.pos+=2
                else:
                    self.lst[self.pos]-=n
                    n=0
                    return self.lst[self.pos+1]
            else:
                return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)