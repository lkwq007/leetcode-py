class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # characters, sorted distinct
        self.char=characters
        self.last=len(characters)-combinationLength
        self.total=len(characters)
        self.idx=list(range(combinationLength))
        self.flag=True
    
    def next(self) -> str:
        ret=""
        for i in self.idx:
            ret+=self.char[i]
        flag=True
        for pos in range(0,len(self.idx)):
            if self.idx[~pos]<self.total+(~pos):
                self.idx[~pos]+=1
                cur=self.idx[~pos]+1
                flag=False
                for i in range(pos-1,-1,-1):
                    self.idx[~i]=cur
                    cur+=1
                break
        if flag:
            self.flag=False
        return ret
                
    def hasNext(self) -> bool:
        return self.flag


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()