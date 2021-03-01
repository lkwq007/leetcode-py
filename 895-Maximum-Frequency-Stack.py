class FreqStack:

    def __init__(self):
        self.record={}
        self.stack={}
        self.max=0

    def push(self, x: int) -> None:
        freq=self.record.get(x,0)+1
        self.record[x]=freq
        if freq not in self.stack:
            self.stack[freq]=[x]
        else:
            self.stack[freq].append(x)
        if freq>self.max:
            self.max=freq

    def pop(self) -> int:
        ret=self.stack[self.max].pop()
        self.record[ret]-=1
        if self.record[ret]==0:
            del self.record[ret]
        if len(self.stack[self.max])<1:
            self.max-=1
        return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()